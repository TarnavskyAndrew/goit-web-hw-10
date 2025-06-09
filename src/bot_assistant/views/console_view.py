from bot_assistant.views.abstract_view import UserView
from bot_assistant.utils.translate import translate
from bot_assistant.utils.decorators import input_error
from colorama import Fore


# ConsoleView - клас для виводу інформації на консоль
class ConsoleView(UserView):

    @input_error
    def display_contact(self, contact):  # Функція виводить інформацію про контакт
        print("\nAll contacts:")
        print(contact)

    @input_error
    def display_help(self):  # Функція виводить список доступних команд
        # print("\n" + translate("help_header"))
        print(f"  {Fore.BLUE}{translate('help_header')}{Fore.RESET}\n")
        for line in translate("help_table").strip().split("\n"):
            # print("  " + line)
            print(f'{Fore.BLUE}{"    " + line}{Fore.RESET}')

    @input_error
    def display_message(self, message):  # Функція виводить повідомлення на консоль
        print(f": {message}")

    @input_error
    def display_welcome_commands(self):
        print (
            "\n" + (f"{Fore.GREEN}{translate('welcome')}{Fore.RESET}") + "\n"
            f": {translate('hint_help_command')}"
        )
