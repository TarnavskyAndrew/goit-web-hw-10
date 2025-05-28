# Конфігурація для вибору мови

selected_lang = "EN"  # default


# функція для встановлення мови інтерфейсу користувача
def set_lang(lang: str):
    global selected_lang
    selected_lang = lang.upper()


# функція для отримання поточної мови інтерфейсу користувача
def get_lang():
    return selected_lang
