from pathlib import Path


# шукає кореневу папку проекта по назві
def find_project_root(project_folder="bot_assistant") -> Path:
    path = Path(__file__).resolve()
    for parent in path.parents:
        if parent.name == project_folder:
            return parent
    raise RuntimeError(f"Project root '{project_folder}' not found from: {path}.")


# повертає абсолютний шляхдо до файлу відносно кореня проекту
def project_path(relative_path: str, project_folder="bot_assistant") -> Path:
    path = find_project_root(project_folder) / relative_path
    return path


# Централізовані змінні шляхів
DATA_DIR = project_path("data")
DATA_DIR_UTILS = project_path("utils")

ADDRESSBOOK_FILE = DATA_DIR / "addressbook.pkl"
BACKUP_FILE = DATA_DIR / "addressbook_bak.pkl"
COUNTRY_CODES_FILE = DATA_DIR / "country_codes.csv"
BACKUP_FILE_MIGRATE = DATA_DIR / "addressbook_bak_migrate.pkl"
PYPROJECT_FILE = DATA_DIR_UTILS / "pyproject.toml"
