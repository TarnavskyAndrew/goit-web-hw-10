import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bot_assistant.utils.path_config import ADDRESSBOOK_FILE, BACKUP_FILE_MIGRATE
from bot_assistant.utils.phone_utils import load_phone_codes
from bot_assistant.models.address_book import AddressBook
from bot_assistant.models.fields import Phone
import shutil

# poetry run python -m bot_assistant.utils.migrate_contacts  - запуск через консоль

# BACKUP_FILE_MIGRATE - шлях до файлу резервної копії адресної книги
# ADDRESSBOOK_FILE - шлях до файлу адресної книги

# створює копію перед оновленням
if os.path.exists(ADDRESSBOOK_FILE):
    shutil.copyfile(ADDRESSBOOK_FILE, BACKUP_FILE_MIGRATE)
    print("> Backup created: addressbook_bak_migrate.pkl")


book = AddressBook.load_data()
phone_codes = (
    load_phone_codes()
)  # A2 -> завантажуємо словник телефонних кодів: {"UA": "+380", "US": "+1", ...}

prefix_to_region = {
    phone_code.replace("+", ""): region_code for region_code, phone_code in phone_codes.items()
}

prefixes_sorted = sorted(prefix_to_region.keys(), key=len, reverse=True)

success_count = 0
fail_count = 0

for record in book.data.values():
    new_phones = []

    for old_phone in record.phones:
        digits_only = "".join(filter(str.isdigit, old_phone.value))
        region_code = None
        user_part = None

        # визначаємо регіон за префіксом
        if digits_only.startswith("380"):
            region_code = "UA"

            user_part = digits_only[3:]
            if user_part.startswith("0"):
                user_part = user_part[1:]

        else:
            for prefix in prefixes_sorted:
                if digits_only.startswith(prefix):
                    region_code = prefix_to_region[prefix]
                    user_part = digits_only[len(prefix) :]
                    break

        if region_code and user_part:
            try:
                new_phone = Phone(user_part, region_code)
                new_phones.append(new_phone)
                success_count += 1
            except Exception as e:
                print(f"Error recreating number {old_phone.value}: {e}")
                fail_count += 1
        else:
            print(f"Failed to determine country for number: {old_phone.value}")
            fail_count += 1

    record.phones = new_phones

AddressBook.save_data(book)
print(f"> Migration completed. Successfully reformatted: {success_count}, failed: {fail_count}")
