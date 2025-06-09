from bot_assistant.models.address_book import AddressBook
from bot_assistant.utils.translate import translate
from bot_assistant.models.record import Record
from bot_assistant.models.fields import Phone
from datetime import datetime
from colorama import Fore
from bot_assistant.utils.logger import logger


# Функція для пошуку запису в адресній книзі за ім'ям та перевірки на коректність введення
# Повертає запис, якщо знайдено, або повідомлення про відсутність контакту
def get_record(name: str, book: AddressBook) -> Record:
    logger.debug("get_record called with name=%s", name)

    validate_name(name)

    record = book.find(name)
    if not record:
        logger.info("Contact not found: %s", name)
        raise ValueError(translate("contact_not_found"))

    logger.debug("Record found: %s", record)
    return record


def validate_name(name: str):
    if not name.strip():
        logger.warning("Empty name detected")
        raise ValueError(translate("empty_name"))
    
    if not name.isalpha():
        logger.warning("Invalid characters in name")
        raise ValueError(translate("invalid_name"))

def validate_phone(phone: str):
    if not phone.isdigit():
        logger.warning("Phone not digit")
        raise ValueError(translate("invalid_number"))
    
    if not is_phone_length_valid(phone):
        logger.warning("Phone number length is not valid")
        raise ValueError(translate("invalid_number_length"))


# Функції для форматування повідомлень про помилки
def format_error(message):
    logger.debug("Formatting error message: %s", message)
    return f"{Fore.RED}-> {message}{Fore.RESET}"

def format_warning(message):
    logger.debug("Formatting warning message: %s", message)
    return f"{Fore.YELLOW}-> {message}{Fore.RESET}"



# Функція перевіряє, чи є номер телефону коректним.
def is_phone_length_valid(phone: str) -> bool:
    digits = "".join(filter(str.isdigit, phone))
    is_valid = 10 <= len(digits) <= 12
    logger.debug("Phone validation: raw=%s, digits=%s, is_valid=%s", phone, digits, is_valid)
    return is_valid


# Функція перевіряє, чи є рядок коректною датою у форматі DD.MM.YYYY.
def is_valid_date(date_str):
    logger.debug("Date validation called for: %s", date_str)
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        logger.warning("Invalid date format: %s", date_str)
        return False


# Функція перевіряє номер телефону та регіон, створює об'єкт Phone.
# Якщо номер телефону некоректний, піднімає ValueError з повідомленням про помилку.
def validate_and_create_phone(phone: str, region: str) -> str:
    logger.debug("Creating phone with phone=%s, region=%s", phone, region)
    try:
        return Phone(phone, region)
    except ValueError as e:
        logger.error("Phone creation failed: %s", str(e))
        raise ValueError(translate("invalid_number_length").format(error=str(e)))
