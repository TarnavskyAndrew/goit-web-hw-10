from colorama import Fore, Style, init
import subprocess
import sys


# Перевірка - стиль, типи та складність за допомогою flake8, mypy та radon:

# pip install flake8 mypy radon
# Додаємо залежності для перевірки коду на стиль, типи та складність:
# poetry add --group dev flake8 mypy radon black

init(autoreset=True)


# Перевірка стилю коду за допомогою flake8
def run_flake8(target="."):
    print(f"{Fore.CYAN} Style check (flake8):{Style.RESET_ALL}")
    result = subprocess.run(["flake8", target], check=False)
    print_result(result)


# Перевірка типів коду за допомогою mypy
def run_mypy(target="."):
    print(f"{Fore.MAGENTA} Type check (mypy):{Style.RESET_ALL}")
    result = subprocess.run(["mypy", target], check=False)
    print_result(result)


# Перевірка складності коду за допомогою radon
def run_radon(target="."):
    print(f"{Fore.YELLOW} Complexity check (radon):{Style.RESET_ALL}")
    result = subprocess.run(["radon", "cc", target, "-a"], check=False)
    print_result(result)


# Вивід результатів перевірки
def print_result(result):
    if result.returncode == 0:
        print(f"{Fore.GREEN} No problems found!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED} Problems found!{Style.RESET_ALL}")


def main():

    check = sys.argv[1] if len(sys.argv) > 1 else ""
    target = sys.argv[2] if len(sys.argv) > 2 else "."

    if check == "flake8":
        run_flake8(target)
    elif check == "mypy":
        run_mypy(target)
    elif check == "radon":
        run_radon(target)
    elif check == "all":
        run_flake8(target)
        run_mypy(target)
        run_radon(target)
    else:
        print(f"{Fore.YELLOW}Usage:{Style.RESET_ALL} python check.py [flake8 | mypy | radon | all]")


if __name__ == "__main__":
    main()

# Використання:

# python dev_utils/check.py flake8   - перевірка стилю коду
# python dev_utils/check.py mypy     - перевірка типів коду
# python dev_utils/check.py radon    - перевірка складності коду

# poetry run run-check all           - всі разом: flake8, mypy, radon

# poetry run run-check <argv> <path>  
