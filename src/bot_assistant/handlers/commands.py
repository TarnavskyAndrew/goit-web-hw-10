# from colorama import Fore, Style
from bot_assistant.utils.logger import logger
from bot_assistant.models.record import Record
from bot_assistant.utils.decorators import input_error
from bot_assistant.utils.translate import translate
from bot_assistant.utils.lang import choose_language
from bot_assistant.utils.region import get_valid_region
from bot_assistant.models.address_book import AddressBook
from bot_assistant.utils.backup import create_backup, restore_backup
from bot_assistant.utils.input_validators import (
    get_record,
    format_error,
    format_warning,
    is_phone_length_valid,
    is_valid_date,
    validate_and_create_phone,
    validate_name,
    validate_phone
)


# Функція додає новий контакт або оновлює існуючий та доадє регіон до номера телефону.
@input_error
def add_contact(args, book):
    logger.debug(f"add_contact called with args: {args}")
    if len(args) < 2:
        logger.warning("Not enough arguments for add_contact.")
        return translate("usage_add")

    name, phone = args[0], args[1]

    try:
        validate_name(name)
        validate_phone(phone)
    except ValueError as e:
        return format_error(str(e)) 
    
    create_backup()

    # Запитуємо регіон
    region = get_valid_region() or "UA"

    try:
        validate_and_create_phone(phone, region)
    except ValueError as e:
        logger.error("Failed to validate and create phone: %s", str(e))
        return format_error(str(e))

    # Перевіряємо, чи є контакт з таким ім'ям...
    try:
        record = get_record(name, book)
    except ValueError as e:
        logger.warning("get_record failed: %s", str(e))            
        record = Record(name)
        book.add_record(record)

    try:
        record.add_phone(phone, region)
    except ValueError as e:
        return format_warning(str(e))
    AddressBook.save_data(book)
    # logger.debug("Record object: %s", record)
    logger.info(f"New contact added: {name}")
    return translate("add_success")


# Функція замінює старий номер телефону на новий для вказаного контакту.
# Якщо контакт не знайдено — повертає повідомлення про помилку.
@input_error
def change_contact(args, book):
    logger.debug(f"Called change_contact with args: {args}")
    if len(args) < 3:
        logger.warning("Not enough arguments provided to change_contact")
        return translate("usage_change")

    name, old_phone, new_phone = args

    try:
        validate_name(name)  
        validate_phone(old_phone)  
        validate_phone(new_phone)
    except ValueError as e:
        return format_error(str(e)) 

    create_backup()

    # Запитуємо регіон
    region = get_valid_region() or "UA"

    try:
        validate_and_create_phone(new_phone, region)
    except ValueError as e:
        logger.error(f"Failed to validate and create phone: {str(e)}")
        return format_error(str(e))

    try:
        record = get_record(name, book)
    except ValueError as e:
        # logger.warning("get_record failed: %s", str(e))
        logger.error("get_record failed during change_contact: %s", str(e))
        return format_error(str(e))

    record.edit_phone(old_phone, new_phone, region)
    AddressBook.save_data(book)
    # logger.debug("Record object: %s", record)
    logger.info(f"Updated phone for contact: {name}")
    return translate("change_success")


# Функція повертає всі номери телефону для вказаного імені.
# Якщо запис не знайдено — повідомляє про це.
@input_error
def show_phone(args, book):
    logger.debug(f"Called show_phone with args: {args}")
    if len(args) < 1:
        logger.warning("Not enough arguments provided to show_phone")
        return translate("usage_show_phone")

    try:
        name = args[0]
        record = get_record(name, book)
    except ValueError as e:
        logger.warning("get_record failed: %s", str(e))
        return format_error(str(e))

    phones = ", ".join([phone.value for phone in record.phones])
    logger.info(f"Contacts returned: {record.name.value}: {phones}")
    return f"{record.name.value}: {phones}"


# Функція виводить всі збережені контакти з номерами телефону та, за наявності, з днем народження.
@input_error
def show_all_contacts(book):
    logger.debug("show_all_contacts called.")
    contacts = book.show_all_contacts()

    if contacts:
        logger.info("All contacts returned.")
        return contacts
    else:
        logger.info("No contacts found in address book.")
        return translate("contact_not_found")


# Функція додає дату народження до існуючого контакту. Формат дати має бути DD.MM.YYYY.
@input_error
def add_birthday(args, book):
    logger.debug(f"Called add_birthday with args: {args}")
    if len(args) < 2:
        logger.warning("Not enough arguments provided to add_birthday")
        return translate("usage_add_birthday")

    name, birthday = args

    if not is_valid_date(birthday):
        logger.error("ERROR: invalid date format for add_birthday")
        return format_error(translate("invalid_date_format"))

    try:
        record = get_record(name, book)
    except ValueError as e:
        logger.warning("get_record failed: %s", str(e))
        return format_error(str(e))

    create_backup()
    record.add_birthday(birthday)
    AddressBook.save_data(book)
    logger.info(f"Birthday added for contact {name}: {birthday}")
    return translate("birthday_added")


# Функція показує дату народження вказаного контакту, якщо вона збережена.
@input_error
def show_birthday(args, book):
    logger.debug(f"Called show_birthday with args: {args}")
    if len(args) < 1:
        logger.warning("Not enough arguments provided to show_birthday")
        return translate("usage_show_birthday")

    try:
        name = args[0]
        record = get_record(name, book)
    except ValueError as e:
        logger.warning("get_record failed: %s", str(e))
        return format_error(str(e))

    if record and record.birthday:
        logger.info(f"Birthday returned: {record.name.value}: {record.birthday.value}")
        return translate("birthday_is").format(name=record.name.value, date=record.birthday.value)
        # return f"{translate('birthday_is')}"
    logger.info("Birthday not found")
    return translate("birthday_not_found")


# Функція повертає список контактів, у яких день народження наступає протягом найближчих 7 днів.
@input_error
def birthdays(args, book):
    logger.debug(f"Called birthdays with args: {args}")
    upcoming = book.get_upcoming_birthdays()
    if upcoming:
        result = "\n".join(
            [
                f"{name} — {translate('greetings')} {date.strftime('%d.%m.%Y')}"
                for name, date in upcoming
            ]
        )
        logger.info("Found %d upcoming birthdays", len(upcoming))
        return result

    logger.info("There are no upcoming birthdays")
    return translate("no_birthdays")


# Функція видаляє контакт з телефонної книги. Якщо контакт не знайдено — повертає повідомлення про помилку.
@input_error
def delete_contact(args, book):
    logger.debug("Called delete_contact with args: %s", args)
    if len(args) < 1:
        logger.warning("Not enough arguments provided to delete_contact")
        return translate("usage_delete")

    try:
        name = args[0]
        record = get_record(name, book)
    except ValueError as e:
        logger.warning("get_record failed: %s", str(e))
        return format_error(str(e))

    create_backup()
    book.delete(name)
    AddressBook.save_data(book)
    logger.info("Deleted contact: %s", record.name.value)
    return translate("delete_contact").format(name=record.name.value)


# Функція змінює мову інтерфейсу користувача.
@input_error
def change_language(args, book):
    logger.debug(f"Called change_language with args: {args}")
    choose_language()
    logger.debug("Language change triggered by user")
    return translate("help_prompt")


# Функція відновлює резервну копію адресної книги з файлу backup.pkl.
@input_error
def restore_command(args, book):
    logger.debug("Called restore_command with args: %s", args)
    result = restore_backup()
    logger.debug("restore_backup() returned: %s", result)
    return result


# # Функція показує список доступних команд.
# @input_error
# def show_help(*args):
#     commands = translate("help_list")
#     header = translate("help_header")
#     return header + "\n" + "\n".join(commands)
