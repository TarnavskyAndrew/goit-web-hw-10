# from colorama import Fore, Style
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
    is_phone_length_valid,
    is_valid_date,
    validate_and_create_phone,
)


# Функція додає новий контакт або оновлює існуючий та доадє регіон до номера телефону.
@input_error
def add_contact(args, book):
    if len(args) < 2:
        return translate("usage_add")

    name, phone = args[0], args[1]

    if not name.strip():
        return format_error(translate("empty_name"))
    if not name.isalpha():
        return format_error(translate("invalid_name"))
    if not phone.isdigit():
        return format_error(translate("invalid_number"))
    if not is_phone_length_valid(phone):
        return format_error(translate("invalid_number_length"))

    create_backup()

    # Запитуємо регіон
    region = get_valid_region() or "UA"

    try:
        validate_and_create_phone(phone, region)
    except ValueError as e:
        return format_error(str(e))

    # Перевіряємо, чи є контакт з таким ім'ям...
    try:
        record = get_record(name, book)
    except ValueError:
        record = Record(name)
        book.add_record(record)

    record.add_phone(phone, region)
    AddressBook.save_data(book)
    return translate("add_success")


# Функція замінює старий номер телефону на новий для вказаного контакту.
# Якщо контакт не знайдено — повертає повідомлення про помилку.
@input_error
def change_contact(args, book):
    if len(args) < 3:
        return translate("usage_change")

    name, old_phone, new_phone = args

    if not name.strip():
        return format_error(translate("empty_name"))
    if not name.isalpha():
        return format_error(translate("invalid_name"))
    if not old_phone.isdigit() and not new_phone.isdigit():
        return translate("invalid_number")
    if not is_phone_length_valid(new_phone):
        return translate("invalid_number_length")

    create_backup()

    # Запитуємо регіон
    region = get_valid_region() or "UA"

    try:
        validate_and_create_phone(new_phone, region)
    except ValueError as e:
        return format_error(str(e))

    try:
        record = get_record(name, book)
    except ValueError as e:
        return format_error(str(e))

    record.edit_phone(old_phone, new_phone, region)
    AddressBook.save_data(book)
    return translate("change_success")


# Функція повертає всі номери телефону для вказаного імені.
# Якщо запис не знайдено — повідомляє про це.
@input_error
def show_phone(args, book):
    if len(args) < 1:
        return translate("usage_show_phone")

    try:
        name = args[0]
        record = get_record(name, book)
    except ValueError as e:
        return format_error(str(e))

    phones = ", ".join([phone.value for phone in record.phones])
    return f"{record.name.value}: {phones}"


# Функція виводить всі збережені контакти з номерами телефону та, за наявності, з днем народження.
@input_error
def show_all_contacts(book):
    return book.show_all_contacts() or translate("contact_not_found")


# Функція додає дату народження до існуючого контакту. Формат дати має бути DD.MM.YYYY.
@input_error
def add_birthday(args, book):
    if len(args) < 2:
        return translate("usage_add_birthday")

    name, birthday = args

    if not is_valid_date(birthday):
        return format_error(translate("invalid_date_format"))

    try:
        record = get_record(name, book)
    except ValueError as e:
        return format_error(str(e))

    create_backup()
    record.add_birthday(birthday)
    AddressBook.save_data(book)
    return translate("birthday_added")


# Функція показує дату народження вказаного контакту, якщо вона збережена.
@input_error
def show_birthday(args, book):
    if len(args) < 1:
        return translate("usage_show_birthday")

    try:
        name = args[0]
        record = get_record(name, book)
    except ValueError as e:
        return format_error(str(e))

    if record and record.birthday:
        return translate("birthday_is").format(name=record.name.value, date=record.birthday.value)
        # return f"{translate('birthday_is')}"
    return translate("birthday_not_found")


# Функція повертає список контактів, у яких день народження наступає протягом найближчих 7 днів.
@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if upcoming:
        return "\n".join(
            [
                f"{name} — {translate('greetings')} {date.strftime('%d.%m.%Y')}"
                for name, date in upcoming
            ]
        )
    return translate("no_birthdays")


# Функція видаляє контакт з телефонної книги. Якщо контакт не знайдено — повертає повідомлення про помилку.
@input_error
def delete_contact(args, book):
    if len(args) < 1:
        return translate("usage_delete")

    try:
        name = args[0]
        record = get_record(name, book)
    except ValueError as e:
        return format_error(str(e))

    create_backup()
    book.delete(name)
    AddressBook.save_data(book)
    return translate("delete_contact").format(name=record.name.value)
    # return f"{Fore.GREEN}{translate('contact_deleted').format(name=record.name.value)}{Style.RESET_ALL}"


# Функція змінює мову інтерфейсу користувача.
@input_error
def change_language(args, book):
    choose_language()
    return translate("help_prompt")


# Функція відновлює резервну копію адресної книги з файлу backup.pkl.
@input_error
def restore_command(args, book):
    return restore_backup()


# # Функція показує список доступних команд.
# @input_error
# def show_help(*args):
#     commands = translate("help_list")
#     header = translate("help_header")
#     return header + "\n" + "\n".join(commands)
