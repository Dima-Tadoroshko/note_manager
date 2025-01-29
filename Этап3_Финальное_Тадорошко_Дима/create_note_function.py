from datetime import datetime, timedelta
# Функция для создания заметки
def create_note():
    print(" Создание новой заметки ")

    # Создание переменной для ввода имя пользователя и цикл для проверки пустых строк
    username = input("Введите имя пользователя: ").strip() # удаление пробелов
    while not username:
        print("Имя пользователя не может быть пустым.")
        username = input("Введите имя пользователя: ").strip()

    # Создание переменной для ввода заголовка и цикл для проверки пустых строк
    title = input("Введите заголовок заметки: ").strip()
    while not title:
        print("Заголовок заметки не может быть пустым.")
        title = input("Введите заголовок заметки: ").strip()

    # Создание переменной для ввода заголовка и цикл для проверки пустых строк
    content = input("Введите описание заметки: ").strip()
    while not content:
        print("Описание заметки не может быть пустым.")
        content = input("Введите описание заметки: ").strip()

    # Выбор статуса заметки из представленных вариантов
    status_options = ["новая", "в процессе", "выполнено"] # переменная для статуса заметок
    # Удаление пробелов и перевод в нижний регистр строки
    status = input(f"Введите статус заметки ({', '.join(status_options)}): ").strip().lower()
    while status not in status_options:
        print(f"Неверный статус. Выберите из имеющихся вариантов: {', '.join(status_options)}.")
        status = input(f"Введите статус заметки ({', '.join(status_options)}): ").strip().lower()
    # Запись текущей даты
    created_date = datetime.now().strftime("%d-%m-%Y")

    ''' Запись дедлайна по умолчанию
    issue_date_default = datetime.now().date()
    issue_date_default_ = issue_date_default + timedelta(days=7)
    issue_date = datetime.strftime(issue_date_default_, "%d-%m-%Y")'''


    # Ввод даты дедлайна с проверкой корректности введенной даты
    issue_date = input("Введите дату дедлайна (ДД-ММ-ГГГГ): ").strip()
    while not validate_date(issue_date): # not True => False
        print("Неверный формат даты. Пожалуйста, используйте формат 'ДД-ММ-ГГГГ'.")
        issue_date_as_str = input("Введите дату дедлайна (ДД-ММ-ГГГГ): ").strip()
        if not validate_date(issue_date_as_str):
            #print("Неверный формат даты. Пожалуйста, используйте формат 'ДД-ММ-ГГГГ'.")
            continue
        issue_date_ = datetime.strptime(issue_date_as_str, "%d-%m-%Y")
        issue_date = datetime.strftime(issue_date_, "%d-%m-%Y")

    note = { # создаем новый словарь
        "username": username.capitalize(),
        "title": title.capitalize(),
        "content": content.capitalize(),
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

    return note

def validate_date(date_str):
    try:
        issue_date = datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def my_notes():
    for i in note:
        print(f"{i}: {note[i]}")

if __name__ == "__main__":
    note = create_note()
    print("\nЗаметка создана:")
    print(note)