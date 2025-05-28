# from colorama import Fore
from bot_assistant.utils.path_config import COUNTRY_CODES_FILE
from bot_assistant.utils.translate import translate
import csv


# Функція завантажує коди країн з CSV файлу та повертає список підтримуваних регіонів (A2 коди).
def load_country_codes(filepath=COUNTRY_CODES_FILE):
    with open(filepath, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row["A2"].strip().upper() for row in reader if row["A2"].strip()]


# Функція запитує у користувача регіон (A2 код країни) та перевіряє його на валідність.
def get_valid_region():
    supported = load_country_codes()

    while True:
        region = input(translate("region_prompt")).strip().upper() or "UA"

        if region in supported:
            return region
        else:
            print(translate("invalid_region").format(region=region))
