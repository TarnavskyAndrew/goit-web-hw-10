from bot_assistant.models.fields import Phone, Name, Birthday
from bot_assistant.utils.translate import translate
from bot_assistant.utils.logger import logger
from colorama import Fore


# 4. Клас запису: описує один запис (контакт): ім'я + список телефонів
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_str, region):
        phone = Phone(phone_str, region)
        formatted = str(phone)        
        if any(str(p) == formatted for p in self.phones):
            logger.warning("Attempt to add duplicate phone: %s", formatted)
            raise ValueError(translate("phone_already_exists").format(phone=phone))   
        else:
            logger.debug("Adding phone %s to %s", phone_str, self.name.value)
            self.phones.append(phone)
            
    def remove_phone(self, phone_str):
        phone = self.find_phone(phone_str)
        if phone:
            self.phones.remove(phone)
            logger.info("Removed phone %s from %s", phone_str, self.name.value)
        else:
            # print(f"Phone '{phone_str}' not found.")
            logger.warning("Attempted to remove non-existing phone: %s", phone_str)
            return None

    def edit_phone(self, old, new, region):
        phone = self.find_phone(old)
        if phone:
            self.remove_phone(old)
            self.add_phone(new, region)
            logger.info("Edited phone %s to %s for %s", old, new, self.name.value)
        else:
            logger.error("Phone number %s not found during edit", old)
            raise ValueError(f"Phone number {old} not found.")

    def find_phone(self, phone_str):
        for phone in self.phones:
            if phone == phone_str:
                return phone
        return None

    def add_birthday(self, birthday_str):
        logger.debug("Adding birthday %s to %s", birthday_str, self.name.value)
        self.birthday = Birthday(birthday_str)

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = f"{self.birthday.value}" if self.birthday else "Not set!"
        return f"{Fore.BLUE} Contact name: {Fore.RESET} {self.name.value}\nPhones: {phones} \nBirthday: {birthday}"
