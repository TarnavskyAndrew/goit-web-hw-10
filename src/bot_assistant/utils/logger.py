from bot_assistant.utils.path_config import PYPROJECT_FILE
from logging.handlers import RotatingFileHandler
from pathlib import Path
from colorama import Fore
import tomllib
import logging
import json


class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps(
            {
                "timestamp": self.formatTime(record, self.datefmt),
                "level": record.levelname,
                "module": record.module,
                "funcName": record.funcName,
                "line": record.lineno,
                "message": record.getMessage(),
            },
            ensure_ascii=False,
        )

def setup_logger():
    config = {}  # by default
    try:
        with open(PYPROJECT_FILE, "rb") as file:
            config = tomllib.load(file).get("tool", {}).get("logging", {})
    except Exception as e:
        print(
            f"{Fore.YELLOW}WARNING: {Fore.RESET}Failed to load logging config from pyproject.toml: {e}, -> using defaults.."
        )
       
    log_level = config.get("level", "DEBUG").upper()
    console_enabled = config.get("console", False)  # console output
    console_level = config.get("console_level", "INFO").upper()
    log_dir = config.get("log_dir", "logs")
    rotation_mb = config.get("rotation_mb", 50)
    backup_count = config.get("backup_count", 2)

    Path(log_dir).mkdir(parents=True, exist_ok=True)
    log_file = Path(log_dir) / "bot_assistant.log"

    logger = logging.getLogger("bot_assistant")

    if logger.hasHandlers():
        logger.handlers.clear()  # Remove any previously attached handlers

    logger.setLevel(log_level)

    # File handler
    file_handler = RotatingFileHandler(
        log_file, maxBytes=1024 * 1024 * rotation_mb, backupCount=backup_count, encoding="utf-8"
    )
    file_handler.setFormatter(JsonFormatter())
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    # Console handler
    if console_enabled:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(JsonFormatter())
        console_handler.setLevel(console_level)
        logger.addHandler(console_handler)

    logger.propagate = False  # Important: Prevent propagation to root logger


# Инициализация при импорте
# setup_logger()
# with open(PYPROJECT_FILE, "rb") as file:
#     parsed = tomllib.load(file)
#     print("FULL TOML PARSED:", parsed)
logger = logging.getLogger("bot_assistant")
