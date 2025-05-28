from bot_assistant.utils.path_config import COUNTRY_CODES_FILE
import csv


# фуекція для завантаження телефонних кодів країн з CSV файлу
def load_phone_codes(filepath=COUNTRY_CODES_FILE):
    codes = {}
    with open(filepath, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            a2 = row["A2"].upper().strip()
            code = row["Phone Code"].strip()
            if a2 and code:
                codes[a2] = code
    return codes
