from bot_assistant.utils.path_config import ADDRESSBOOK_FILE, BACKUP_FILE, BACKUP_FILE_MIGRATE
from bot_assistant.utils.input_validators import format_error
from bot_assistant.utils.translate import translate
from bot_assistant.utils.logger import logger
import shutil
import os


# BACKUP_FILE_MIGRATE - Якщо використовується міграція
# BACKUP_FILE - Файл резервної копії адресної книги
# ADDRESSBOOK_FILE - Основний файл адресної книги


# Створює резервну копію адресної книги, якщо файл адресної книги існує.
def create_backup():
    if os.path.exists(ADDRESSBOOK_FILE):
        try:
            shutil.copyfile(ADDRESSBOOK_FILE, BACKUP_FILE)
            logger.info("Backup created successfully")
            print("Backup created")
        except Exception as e:
            logger.error(f"Failed to create backup: {e}")
            return format_error(str(e))


# Відновлення резервної копії адресної книги
def restore_backup():
    if not os.path.exists(BACKUP_FILE):
        return translate("no_backup")
    else:
        try:
            shutil.copyfile(BACKUP_FILE, ADDRESSBOOK_FILE)
            logger.info("Backup restored successfully")
            return translate("restore_success")
        except Exception as e:
            logger.critical(f"Critical: failed to restore backup: {e}")
            return translate("restore_failed")
        
