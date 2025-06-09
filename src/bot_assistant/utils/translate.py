from bot_assistant.utils.config import get_lang
from bot_assistant.utils.logger import logger

# модуль забезпечує переклади повідомлень бота-помічника, містить словник з перекладами різними мовами.

translations = {
    "EN": {
        "welcome": "Welcome to the assistant bot!",
        "hint_help_command": "Type 'help' to see what I can do.",
        "goodbye": "Goodbye, have a nice day!",
        "region_prompt": "Enter region code (press Enter for UA): ",
        "add_success": "Contact added.",
        "change_success": "Phone updated.",
        "contact_not_found": "Contact not found.",
        "empty_input": "Empty input. Type a command like 'hello' or 'help'.",
        "help_prompt": "Hello! How can I help you?",
        "enter_a_command": "Enter a command:",
        "show_all_contacts": "Showing all contacts:",
        "delete_contact": "Contact: {name} deleted.",
        "show_birthday_result": "Birthday for {name}: {date}",
        "no_birthday_set": "No birthday set for this contact.",
        "upcoming_birthdays_header": "Upcoming birthdays this week:",
        "no_birthdays": "There are no upcoming birthdays.",
        "birthday_added": "Birthday added successfully.",
        "birthday_not_found": "Birthday not found.",
        "birthday_is": "{name} birthday is {date}",
        "birthday_not_set": "Birthday not set.",
        "greetings": "Greetings:",
        "language_set": "Language set: {lang} ({label})",
        "region_prompt": "Select the country for correct number formatting (e.g. UA, US, DE). Enter — UA: ",
        "invalid_region": 'Region "{region}" is not supported. Try again.',
        "usage_change": "Usage: change <name> <old_phone> <new_phone>",
        "invalid_number_length": "The phone number must contain 10 to 12 digits (without country code). For UA, start with «0».",
        "invalid_number": "Invalid phone number. Must contain only digits.",
        "usage_show_phone": "Usage: phone <name>",
        "usage_show_birthday": "Usage: show-birthday <name>",
        "usage_add_birthday": "Usage: add-birthday <name> <DD.MM.YYYY>",
        "usage_delete": "Usage: delete <name>",
        "usage_add": "Usage: add <name> <phone>",
        "full_number_length_error": "The full number must contain between 10 and 15 digits.",
        "invalid_ukrainian_number": "The number must consist of 10 digits and start with «0» (eg 0671234567)",
        "region_code_not_found": "Telephone code for region {region} not found.",
        "digits_range_error": "Enter from 10 to 12 digits without the country code (it will be added automatically).",
        "invalid_name": "Name must contain only letters.",
        "invalid_date_format": "Date must be in format DD.MM.YYYY.",
        "empty_name": "Name cannot be empty.",
        "invalid_command_with_help": "Invalid command. Type a command 'help' to see available commands.",
        "invalid_command": "Invalid command.",
        "restore_success": "Address book successfully restored from backup.",
        "restore_failed": "Failed to restore backup.",
        "no_backup": "No backup file found.",
        "no_contacts_yet": "No contacts yet.",
        "phone_already_exists": "Phone: {phone} already exists for this contact",
        # "language_set": "Language set: {lang}",
        "help_header": "Available commands:",
        "help_table": """        

hello           — Greeting                 | hello
add             — Add a contact            | add <name> <phone>
change          — Change phone             | change <name> <old> <new>
phone           — Show contact phones      | phone <name>
all             — Show all contacts        | all
add-birthday    — Add birthday             | add-birthday <name> <DD.MM.YYYY>
show-birthday   — Show birthday            | show-birthday <name>
birthdays       — Birthdays this week      | birthdays
delete          — Delete contact           | delete <name>
help            — List commands            | help
lang            — Change language          | lang
exit / close    — Exit the assistant       | exit / close
restore         — Restore backup           | restore
    """
    },
    "UA": {
        "welcome": "Ласкаво просимо до бота-помічника!",
        "hint_help_command": "Введіть «help», щоб дізнатися, що я можу зробити.",
        "goodbye": "До побачення! Гарного дня!",
        "region_prompt": "Введіть код країни (натисніть Enter для UA): ",
        "add_success": "Контакт додано.",
        "change_success": "Номер оновлено.",
        "contact_not_found": "Контакт не знайдено.",
        "empty_input": "Порожній ввід. Введіть команду, наприклад 'hello' або 'help'.",
        "help_prompt": "Привіт! Чим можу допомогти?",
        "enter_a_command": "Введіть команду:",
        "show_all_contacts": "Показ усіх контактів:",
        "delete_contact": "Контакт: {name} видалено.",
        "show_birthday_result": "День народження для {name}: {date}",
        "no_birthday_set": "Для цього контакту день народження не встановлено.",
        "upcoming_birthdays_header": "Наближаються дні народження цього тижня:",
        "no_birthdays": "У найближчі 7 днів немає днів народження.",
        "birthday_added": "День народження успішно додано.",
        "birthday_not_found": "День народження не знайдено.",
        "birthday_is": "День народження {name} — {date}",
        "birthday_not_set": "День народження не встановлено.",
        "greetings": "Вітання:",
        "language_set": "Мову встановлено: {lang} ({label})",
        "region_prompt": "Оберіть країну для правильного форматування номера (наприклад UA, US, DE). Enter — UA: ",
        "invalid_region": 'Регіон "{region}" не підтримується. Спробуйте ще раз.',
        "usage_change": "Використання: change <ім’я> <старий_номер> <новий_номер>",
        "invalid_number_length": "Номер телефону має містити від 10 до 12 цифр (без коду країни). Для UA — починається з «0».",
        "invalid_number": "Недійсний номер телефону. Повинен містити лише цифри.",
        "usage_show_phone": "Використання: phone <ім’я>",
        "usage_show_birthday": "Використання: show-birthday <ім’я>",
        "usage_add_birthday": "Використання: add-birthday <ім’я> <DD.MM.YYYY>",
        "usage_delete": "Використання: delete <ім’я>",
        "usage_add": "Використання: add <ім’я> <номер>",
        "full_number_length_error": "Повний номер повинен містити від 10 до 15 цифр.",
        "invalid_ukrainian_number": "Номер має складатися з 10 цифр та починатися з «0» (наприклад, 0671234567)",
        "region_code_not_found": "Телефонний код для регіону {region} не знайдено.",
        "digits_range_error": "Введіть від 10 до 12 цифр без коду країни (він додасться автоматично).",
        "invalid_name": "Ім’я повинно містити лише літери.",
        "invalid_date_format": "Дата повинна бути у форматі DD.MM.YYYY.",
        "empty_name": "Ім’я не може бути порожнім.",
        "invalid_command_with_help": "Невідома команда. Введіть команду 'help', щоб побачити доступні команди.",
        "invalid_command": "Невідома команда.",
        "restore_success": "Адресну книгу успішно відновлено з резервної копії.",
        "restore_failed": "Не вдалося відновити резервну копію.",
        "no_backup": "Файл резервної копії не знайдено.",
        "no_contacts_yet": "Поки що немає контактів.",
        "phone_already_exists": "Телефон: {phone} вже існує для цього контакту",        
        "help_header": "Доступні команди:",
        "help_table": """
            
hello           — Привітання                    | hello
add             — Додати контакт                | add <ім'я> <телефон>
change          — Змінити номер                 | change <ім'я> <старий> <новий>
phone           — Показати номери контакту      | phone <ім'я>
all             — Всі контакти                  | all
add-birthday    — Додати день народження        | add-birthday <ім'я> <ДД.ММ.РРРР>
show-birthday   — Показати день народження      | show-birthday <ім'я>
birthdays       — Дні народження цього тижня    | birthdays
delete          — Видалити контакт              | delete <ім'я>
help            — Список команд                 | help
lang            — Змінити мову                  | lang
exit / close    — Вихід з бота                  | exit / close
restore         — Відновити резервну копію      | restore
    """
    },
}


def translate(key: str) -> str | list:
    # logger.debug(f"Called translate with args: {key}")
    logger.debug("translate called with key: %s", key)

    lang = get_lang()
    result = translations.get(lang, {}).get(key, key)
    logger.debug("translate result for lang %s and key %s: %s", lang, key, result)
    return result


# print(translate("language_set").format(lang=get_lang()))
