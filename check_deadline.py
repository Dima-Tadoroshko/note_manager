from datetime import datetime

#Вывод на экран сегоднешней даты формате дд-мм-гггг
day = datetime.now().date()
day_2 = day.strftime("%d-%m-%Y")
print(f"Текущая дата: \n", day_2)

while True:
    try:
        #Запрос у пользователя даты дедлайна и запись даты в переменную
        issue_date = input("Введите дату дедлайна, в формате ДД-ММ-ГГГГ: ")

        deadline_data = datetime.strptime(issue_date, "%d-%m-%Y").date()
        #Создание переменной для текущей даты и вычисления сроков дедлайна
        current_time = datetime.now().date()
        time_difference = deadline_data - current_time
        days_difference = time_difference.days
        # Проверка результата дедлайна и вывод соответствуещего значения
        if days_difference < 0:
            print(f"Внимание! Дедлайн истек {abs(days_difference):02d} дней назад.")
        elif days_difference == 0:
            print('Дедлайн сегодня!')
        else:
            print(f"До дедлайна осталось {days_difference:02d} дней.")
        break
    # Проверка корректности ввода данных пользователем
    except ValueError:
        print("Ошибка! Убедитесь, что вводите правильную дату в формате, ДД-ММ-ГГГГ.")
        print("Например, 15-01-2025")
    # Остальные ошибки
    except Exception as e:
        print(f'Произошла непредвиденная ошибка: {str(e)}')
        print("Пожалуйста, попробуйте снова")