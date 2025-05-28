from bot_assistant.utils.config import set_lang
from bot_assistant.utils.translate import translate
from colorama import Fore
import sys


# Функція вибирає мову інтерфейсу користувача та встановлює її.
def choose_language():

    LANGUAGES = {"UA": "Українська", "EN": "English"}
    # Цикл для вибору мови, який продовжується, поки користувач не вибере правильну мову або не вийде з програми
    while True:
        print(f"\n{Fore.BLUE}>{Fore.RESET} Select language:")
        for code, label in LANGUAGES.items():
            print(f"[{code}] {label}")

        choice = input("Your choice (press Enter for EN): ").strip().upper()

        if choice in ("EXIT", "CLOSE"):
            print(f"{Fore.GREEN}{translate('goodbye')}{Fore.RESET}")
            sys.exit()

        if not choice:
            choice = "EN"

        if choice in LANGUAGES:
            set_lang(choice)
            print(
                f"{Fore.BLUE}> {Fore.RESET}{translate('language_set').format(lang=choice, label=LANGUAGES[choice])}"
            )
            break
        else:
            print("Invalid choice. Try again.")
