from bot_assistant.models.address_book import AddressBook
from bot_assistant.utils.translate import translate
from bot_assistant.models.record import Record
from bot_assistant.models.fields import Phone
from datetime import datetime
from colorama import Fore


# Функція для пошуку запису в адресній книзі за ім'ям та перевірки на коректність введення
# Повертає запис, якщо знайдено, або повідомлення про відсутність контакту
def get_record(name: str, book: AddressBook) -> Record:

    if not name.strip():
        raise ValueError(translate("empty_name"))

    if not name.isalpha():
        raise ValueError(translate("invalid_name"))

    record = book.find(name)
    if not record:
        raise ValueError(translate("contact_not_found"))

    return record


# Функція для форматування повідомлень про помилки
def format_error(message):
    return f"{Fore.RED}-> {message}{Fore.RESET}"


# Функція перевіряє, чи є номер телефону коректним.
def is_phone_length_valid(phone: str) -> bool:
    digits = "".join(filter(str.isdigit, phone))
    return 10 <= len(digits) <= 12


# Функція перевіряє, чи є рядок коректною датою у форматі DD.MM.YYYY.
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False


# Функція перевіряє номер телефону та регіон, створює об'єкт Phone.
# Якщо номер телефону некоректний, піднімає ValueError з повідомленням про помилку.
def validate_and_create_phone(phone: str, region: str) -> str:
    try:
        return Phone(phone, region)
    except ValueError as e:
        raise ValueError(translate("invalid_number_length").format(error=str(e)))
