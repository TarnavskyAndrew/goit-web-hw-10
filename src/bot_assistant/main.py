from colorama import Fore
from bot_assistant.utils.logger import setup_logger, logger
from bot_assistant.models.address_book import AddressBook
from bot_assistant.views.console_view import ConsoleView
from bot_assistant.utils.lang import choose_language
from bot_assistant.utils.translate import translate
from bot_assistant.handlers.commands import (
    add_contact,
    change_contact,
    show_phone,
    show_all_contacts,
    add_birthday,
    show_birthday,
    birthdays,
    delete_contact,
    change_language,
    restore_command,
    # show_help
)

# poetry run run-bot - запуск через консоль


# Функція обробляє ввід користувача, розділяючи його на команду та аргументи..````
def parse_input(user_input):
    parts = user_input.strip().split()

    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args


def main():
    setup_logger()
    logger.info("Bot Assistant started")
    
    view = ConsoleView()
    # view.display_welcome_commands()
    view.display_message(f"{Fore.GREEN}{translate('welcome')}{Fore.RESET}")

    choose_language()
    # view.display_message(translate("language_set"))

    book = AddressBook.load_data()

    was_invalid_once = False
    
    view.display_message(f" {translate('hint_help_command')}")

    while True:
        user_input = input((f"{Fore.YELLOW}> {Fore.RESET}{translate('enter_a_command')}"))
        command, args = parse_input(user_input)

        if not command:
            view.display_message(f"{Fore.YELLOW}{translate('empty_input')}{Fore.RESET}")
            continue

        if command in ["close", "exit"]:
            AddressBook.save_data(book)
            view.display_message(f"{Fore.GREEN}{translate('goodbye')}{Fore.RESET}")
            break

        elif command == "hello":  # hello – вітання від бота.
            view.display_message(translate("help_prompt"))

        elif command == "add":
            view.display_message(add_contact(args, book))

        elif command == "change":
            view.display_message(change_contact(args, book))

        elif command == "phone":
            view.display_message(show_phone(args, book))

        elif command == "all":
            view.display_contact(show_all_contacts(book))

        elif command == "add-birthday":
            view.display_message(add_birthday(args, book))

        elif command == "show-birthday":
            view.display_message(show_birthday(args, book))

        elif command == "birthdays":
            view.display_message(birthdays(args, book))

        elif command == "delete":
            view.display_message(delete_contact(args, book))

        elif command == "help":
            view.display_help()

        elif command == "lang":
            view.display_message(change_language(args, book))

        elif command == "restore":
            view.display_message(restore_command(args, book))
            book = AddressBook.load_data()

        else:
            if not was_invalid_once:
                view.display_message(
                    f"{Fore.YELLOW}{translate('invalid_command_with_help')}{Fore.RESET}"
                )
                was_invalid_once = True
            else:
                view.display_message(translate("invalid_command"))


if __name__ == "__main__":
    main()
