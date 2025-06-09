# from colorama import Fore
from bot_assistant.utils.path_config import COUNTRY_CODES_FILE
from bot_assistant.utils.translate import translate
from bot_assistant.utils.logger import logger
import csv


# Функція завантажує коди країн з CSV файлу та повертає список підтримуваних регіонів (A2 коди).
def load_country_codes(filepath=COUNTRY_CODES_FILE):
    try:
        with open(filepath, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            result = [row["A2"].strip().upper() for row in reader if row["A2"].strip()]
            logger.debug("Loaded %d country codes from %s", len(result), filepath)
            return result
    except Exception as e:
        logger.error("Failed to load country codes from %s: %s", filepath, str(e))
        return []

# Функція запитує у користувача регіон (A2 код країни) та перевіряє його на валідність.
def get_valid_region():
    supported = load_country_codes()

    while True:
        region = input(translate("region_prompt")).strip().upper() or "UA"
        logger.debug("User input for region: %s", region)

        if region in supported:
            logger.info("Valid region selected: %s", region)
            return region
        else:
            logger.warning("Invalid region entered: %s", region)
            print(translate("invalid_region").format(region=region))
