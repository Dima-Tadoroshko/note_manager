from datetime import datetime


print(f'Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
notes = []
# Создаем словарь для ввода заметок c проверкой корректности данных
def cr_note():
    #notes.append(cr_note())
    while True: # запрос у пользователя имени и проверка на пустоту введенных данных
        name = input("Введите имя пользователя: ")
        if name == ' ' or name == '':
                print('Данные не введены. Попробуйте снова.')
        else:
            break
    while True:# запрос у пользователя заголовка и проверка на пустоту введенных данных
         title = input("Введите заголовок заметки: ")
         if title == ' ' or title == '':
                print('Данные не введены. Попробуйте снова.')
         else:
            break

    while True:# запрос у пользователя описание заметки и проверка на пустоту введенных данных
        description = input('Введите описание заметки: ')
        if description == ' ' or description == '':
            print('Данные не введены. Попробуйте снова.')
        else:
            break

    while True: #Запрос у пользователя статуса с проверкой корректности введенных данных
        status = input("Введите статус заметки ('новая', 'в процессе', 'выполнена' ): ")
        try:
            if status == 'новая' or status == 'в процессе' or status == 'выполнена':
                break
            else:
                print('Ошибка! Введите корректные данные')
        except ValueError:
            print('Внимание! Введены неправильные данные.')
    while True: # Запрос даты создания с проверкой корректности данных
        create_date = input("Введите дату создания, в формате ДД-ММ-ГГГГ: ")
        try:
            create_date = datetime.strptime(create_date, "%d-%m-%Y").date()
            create_date_2 = create_date.strftime("%d-%m-%Y")
            break
        # Проверка корректности ввода данных пользователем
        except ValueError:
            print("Ошибка! Убедитесь, что вводите правильную дату в формате, ДД-ММ-ГГГГ.")
            print("Например, 15-01-2025")
    while True:# Запрос даты создания с проверкой корректности данных
        issue_date = input("Введите дату дедлайна, в формате ДД-ММ-ГГГГ: ")
        try:
            issue_date = datetime.strptime(issue_date, "%d-%m-%Y").date()
            deadline = issue_date.strftime("%d-%m-%Y")
            break
        # Проверка корректности ввода данных пользователем
        except ValueError:
            print("Ошибка! Убедитесь, что вводите правильную дату в формате, ДД-ММ-ГГГГ.")
            print("Например, 15-01-2025")
# Создание словоря из введенных данных
    return {
        'Имя' : name.capitalize(),
        'Заголовок' : title.capitalize(),
        'Описание' : description.capitalize(),
        'Статус' : status.capitalize(),
        'Дата создания' : create_date_2,
        'Дата дедлайна': deadline
    }
# запиь первой заметки в список
note_ = cr_note()
notes.append(note_)
#print(notes)
#print(note_)
# Функция по выводу всех заметок
def my_notes(notes):
    if not notes:
        print('Нет сохранненых заметок')
        return
    for i, note in enumerate(notes):
        print(f"\nЗаметка № {i + 1}")
        for key, value in note.items():
            print(f"{key}: {value}")
# Функция по добавлению заметок
def main():
    while True:
        command = input('\nХотите добавить ещё одну заметку? (да/нет): ').lower()
        if command == 'да':
            new_note = cr_note()
            notes.append(new_note)
            print('Заметка добавленна')
            #print(notes)
        elif command == "нет":
            print(f'\nСписок заметок:')
            break
        else:
            print("Неверная команда, попробуйте ещё раз")
    my_notes(notes)
if __name__ == '__main__':
    main()