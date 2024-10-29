def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Помилка: Введіть 'add [ім'я] [номер телефону]'"
    name, phone = args
    contacts[name] = phone
    return f"Контакт '{name}' додано з номером {phone}."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Помилка: Введіть 'change [ім'я] [новий номер телефону]'"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Номер телефону контакту '{name}' оновлено на {phone}."
    else:
        return f"Контакт '{name}' не знайдено."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Помилка: Введіть 'phone [ім'я]'"
    name = args[0]
    if name in contacts:
        return f"Номер телефону '{name}': {contacts[name]}"
    else:
        return f"Контакт '{name}' не знайдено."

def show_all(contacts):
    if not contacts:
        return "Записник порожній."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Ласкаво просимо до бота-асистента!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Чим я можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()
