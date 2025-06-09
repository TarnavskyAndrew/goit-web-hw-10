from bot_assistant.utils.path_config import COUNTRY_CODES_FILE
from bot_assistant.utils.logger import logger
import csv


# функція для завантаження телефонних кодів країн з CSV файлу
def load_phone_codes(filepath=COUNTRY_CODES_FILE):
    codes = {}
    try:
        with open(filepath, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                a2 = row["A2"].upper().strip()
                code = row["Phone Code"].strip()
                if a2 and code:
                    codes[a2] = code
        logger.debug("Loaded %d phone codes from %s", len(codes), filepath)            
        return codes
    
    except Exception as e:
        logger.error("Failed to load phone codes from %s: %s", filepath, str(e))
        return {}
