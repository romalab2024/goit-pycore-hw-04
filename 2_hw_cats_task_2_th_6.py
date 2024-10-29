def get_cats_info(path):
    cats = []
    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            # Читаємо кожен рядок файлу
            for line in file:
                # Розділяємо рядок на ідентифікатор, ім'я та вік
                cat_id, name, age = line.strip().split(',')
                # Створюємо словник для кота
                cat_info = {"id": cat_id, "name": name, "age": age}
                # Додаємо словник до списку котів
                cats.append(cat_info)
        return cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except ValueError:
        print("Помилка у форматі даних.")
        return []

# Приклад використання функції
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
