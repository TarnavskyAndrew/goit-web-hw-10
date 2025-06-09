from bot_assistant.utils.phone_utils import load_phone_codes
from bot_assistant.utils.translate import translate
from bot_assistant.utils.logger import logger
from datetime import datetime


# 1. Базовий клас для всіх полів запису
class Fields:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# 2. Клас імені - обов'язкове поле
class Name(Fields):
    pass


# 3. Клас телефону з валідацією номера
class Phone:
    def __init__(self, phone, region="UA"):
        self.region = region.upper()
        logger.debug("Initializing Phone with number: %s and region: %s", phone, self.region)
        self.value = self.format_phone(phone)

    def format_phone(self, phone):
        phone_codes = load_phone_codes()
        user_digits = "".join(filter(str.isdigit, phone))

        # Якщо регіон - Україна (UA)

        if self.region == "UA":
            return self.format_ukrainian(user_digits)
        else:
            return self.format_international(user_digits, phone_codes)

    def format_ukrainian(self, user_digits):  # форматування номера телефону для України
        logger.debug("Formatting Ukrainian phone number: %s", user_digits)
        if len(user_digits) == 10 and user_digits.startswith("0"):
            user_digits = user_digits[1:]
        elif len(user_digits) != 9:
            logger.warning("Invalid Ukrainian number format: %s", user_digits)
            raise ValueError(translate("invalid_ukrainian_number"))

        code = "+380"
        operator = user_digits[:2]  # 67
        rest = user_digits[2:]  # 1234567

        return f"{code}({operator}){rest[:3]}-{rest[3:5]}-{rest[5:]}"  # +380(67)123-45-67

    # Якщо регіон - форматування номера телефону для інших країн:

    def format_international(self, user_digits, phone_codes):  
        logger.debug("Formatting international phone: %s", user_digits)
        code = phone_codes.get(self.region, "")
        if not code:            
            logger.error("Phone code not found for region: %s", self.region)
            raise ValueError(translate("region_code_not_found").format(region=self.region))

        # Стандарт ITU-T E.164: 10–15 цифр (включачи код країни)
        # Введений номер телефону без коду країни
        if len(user_digits) < 10 or len(user_digits) > 12:
            raise ValueError(translate("digits_range_error"))

        digits = code.replace("+", "") + user_digits

        # Повний номер телефону, включаючи код країни
        if len(digits) < 10 or len(digits) > 15:
            raise ValueError(translate("full_number_length_error"))

        # Розбиваємо: внутрішній код, номер
        internal = digits[len(code) - 1 : len(code) + 2]
        rest = digits[len(code) + 2 :]

        # Форматування.
        if len(rest) == 6:
            return f"{code}({internal}){rest[:3]}-{rest[3:]}"  # +1(501)123-456
        elif len(rest) == 7:
            return f"{code}({internal}){rest[:3]}-{rest[3:5]}-{rest[5:]}"  # +1(501)123-45-67
        elif 8 <= len(rest) <= 10:
            return f"{code}({internal}){rest[:3]}-{rest[3:6]}-{rest[6:]}"  # +1(501)123-456-789
        else:
            return f"{code}({internal}){rest}"  # +1(501)123456789

    def normalized(self):  # повертає номер телефону без форматування
        return "".join(filter(str.isdigit, self.value))

    def __eq__(self, other):  # перевірка на рівність телефонів
        if isinstance(other, Phone):
            return self.normalized() == other.normalized()
        elif isinstance(other, str):
            return self.normalized() == "".join(filter(str.isdigit, other))
        return False

    def __str__(self):
        return self.value


# 4. Клас з датою народження, додає перевірку формату дати DD.MM.YYYY.
class Birthday(Fields):

    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            logger.debug("Parsed birthday: %s", value)
            super().__init__(value)
        except ValueError:
            logger.error("Invalid birthday format: %s", value)
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
