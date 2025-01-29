import datetime

def validate_date(date_str):
    try:
        # Проверка правильности введенной даты
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def update_note(note):
    # Функция обновления данных заметки
    print("==== Обновление заметки ====")
    print("Текущие данные заметки:")
    for key, value in note.items():
        print(f"{key}: {value}")

    updatable_fields = ["username", "title", "content", "status", "issue_date"]

    while True: # Цикл для проверки результатов ввода и запись измененных данных
        field = input(f"\nКакие данные вы хотите обновить? ({', '.join(updatable_fields)}): ").strip().lower()

        if field not in updatable_fields:
            print(f"Ошибка: Поле '{field}' не найдено. Пожалуйста, выберите поле из списка.")
            continue

        # Проверка значений для дедлайна и статуса
        if field == "issue_date":
            new_value = input(f"Введите новое значение для {field} (ДД-ММ-ГГГГ): ").strip()
            if not validate_date(new_value):
                print("Ошибка: Неверный формат даты. Используйте формат 'ДД-ММ-ГГГГ'.")
                continue
            note[field] = new_value
            # new_value = new_value_
            print(f"\nЗаметка успешно обновлена: {field} -> {new_value}")
        elif field == "status":
            status_options = ["новая", "в процессе", "выполнено"]  # переменная для статуса заметок
            # Удаление пробелов и перевод в нижний регистр строки
            new_value = input(f"Введите новый статус заметки ({', '.join(status_options)}): ").strip().lower()
            while new_value not in status_options:
                print(f"Неверный статус. Выберите из имеющихся вариантов: {', '.join(status_options)}.")
                new_value = input(f"Введите новый статус заметки ({', '.join(status_options)}): ").strip().lower()
            note[field] = new_value
                #new_value = new_value_
            print(f"\nЗаметка успешно обновлена: {field} -> {new_value}")

            pass # Остановка цикла while
        else: # Ввод остальных значений для изменения
            new_value = input(f"Введите новое значение для {field}: ").strip().capitalize()
            if not new_value:
                print(f"Ошибка: Значение для {field} не может быть пустым.")
                continue
            update_note_ = input("Вы действительно хотите обновить заметку? (да/нет): ")

            while True:
                if update_note_ == "да":
                    if not new_value:
                        print(f"Ошибка: Значение для {field} не может быть пустым.")
                        continue
                    note[field] = new_value
                    print(f"\nЗаметка успешно обновлена: {field} -> {new_value}")
                    break
                elif update_note_ == "нет":
                    print("Обновление отменено")
                    new_value = note[field]
                    break
                else:
                    print('Введены некорректные данные.')
                    break

                #if not new_value:
                    #print(f"Ошибка: Значение для {field} не может быть пустым.")
                #continue



        #note[field] = new_value
        #print(f"\nЗаметка успешно обновлена: {field} -> {new_value}")

        another_update = input("\nХотите обновить ещё одно поле? (да/нет): ").strip().lower()
        if another_update != "да":
            break

    return note


if __name__ == "__main__":
    note = {
        "username": "Дмитрий",
        "title": "Список покупок",
        "content": "Купить запчасти на машину",
        "status": "новая",
        "created_date": "29-01-2025",
        "issue_date": "30-01-2025"
    }

    updated_note = update_note(note)
    print("\nОбновлённая заметка:")
    print(updated_note)