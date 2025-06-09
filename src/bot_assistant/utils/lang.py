from bot_assistant.utils.config import set_lang
from bot_assistant.utils.translate import translate
from bot_assistant.utils.logger import logger
from colorama import Fore
import sys


# Функція вибирає мову інтерфейсу користувача та встановлює її.
def choose_language():
    logger.debug("Starting language selection...")

    LANGUAGES = {"UA": "Українська", "EN": "English"}
    # Цикл для вибору мови, який продовжується, поки користувач не вибере правильну мову або не вийде з програми
    while True:
        print(f"\n{Fore.BLUE}>{Fore.RESET} Select language:")
        for code, label in LANGUAGES.items():
            print(f"[{code}] {label}")

        choice = input("Your choice (press Enter for EN): ").strip().upper()
        logger.debug("User language input: %s", choice)

        if choice in ("EXIT", "CLOSE"):
            logger.info("User chose to exit during language selection.")
            print(f"{Fore.GREEN}{translate('goodbye')}{Fore.RESET}")
            sys.exit()

        if not choice:
            choice = "EN"

        if choice in LANGUAGES:
            set_lang(choice)
            logger.info("Language set to: %s (%s)", choice, LANGUAGES[choice])
            print(
                f"{Fore.BLUE}> {Fore.RESET}{translate('language_set').format(lang=choice, label=LANGUAGES[choice])}"
            )
            break
        else:
            logger.warning("Invalid language choice entered: %s", choice)
            print("Invalid choice. Try again.")
