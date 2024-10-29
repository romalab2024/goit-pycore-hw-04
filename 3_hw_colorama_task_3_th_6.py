import sys
import os
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізуємо Colorama для кросплатформного кольорового виведення
init(autoreset=True)

def print_directory_structure(directory: Path, indent: str = ''):
    # Перевіряємо, чи шлях є директорією
    if not directory.is_dir():
        print(Fore.RED + f"{directory} - це не директорія або не існує.")
        return

    # Отримуємо вміст директорії
    for item in directory.iterdir():
        if item.is_dir():
            print(Fore.BLUE + f"{indent}📂 {item.name}")
            print_directory_structure(item, indent + '    ')
        else:
            print(Fore.GREEN + f"{indent}📜 {item.name}")

def main():
    # Отримуємо шлях до директорії як аргумент командного рядка
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
        return

    path = Path(sys.argv[1])

    # Перевірка на існування шляху та запуск функції для виведення структури
    if path.exists() and path.is_dir():
        print(Fore.CYAN + f"Структура директорії '{path}':")
        print_directory_structure(path)
    else:
        print(Fore.RED + "Помилка: вказаний шлях не існує або не є директорією.")

if __name__ == "__main__":
    main()
