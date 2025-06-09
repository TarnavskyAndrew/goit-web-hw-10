from bot_assistant.utils.logger import logger
from colorama import Fore


# Декоратор для обробки помилок вводу користувача
def input_error(func):
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except (IndexError, ValueError, KeyError) as e:
            logger.warning("Handled input error in %s: %s", func.__name__, str(e))
            return f"{Fore.RED}[ERROR:]{Fore.RESET} {e}"

    return inner
