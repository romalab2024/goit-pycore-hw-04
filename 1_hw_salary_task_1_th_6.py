def total_salary(path):
    try:
        # Відкриваємо файл та ініціалізуємо змінні для підрахунку
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            # Читаємо кожен рядок файлу
            for line in file:
                # Розділяємо рядок на прізвище та зарплату
                _, salary = line.strip().split(',')
                # Додаємо зарплату до загальної суми та збільшуємо лічильник розробників
                total += int(salary)
                count += 1

            # Обчислюємо середню зарплату
            average = total / count if count > 0 else 0
            return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except ValueError:
        print("Помилка у форматі даних.")
        return 0, 0

# Приклад використання функції
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
