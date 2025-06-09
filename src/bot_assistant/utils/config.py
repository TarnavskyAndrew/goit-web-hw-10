from bot_assistant.utils.logger import logger


# Конфігурація для вибору мови
selected_lang = "EN"  # default


# функція для встановлення мови інтерфейсу користувача
def set_lang(lang: str):
    global selected_lang
    selected_lang = lang.upper()
    logger.info("Language set to: %s", selected_lang)


# функція для отримання поточної мови інтерфейсу користувача
def get_lang():
    logger.debug("Requested current language: %s", selected_lang)
    return selected_lang
