from datetime import datetime

# Функция сортировки даты создания
def sort_note(x):
    return x["created_date"]

# Функция вывода списка на экран
def display_page(notes, page):
    start_index = 0 + page * 5
    end_index = 5 + page * 5
                                # notes[0:5] - первая страница
                                # notes[5:10] - вторая страница
    for index, note in enumerate(notes, start=1):  # notes [start_index:end_index] постраничный вывод
        print(f"""
        Номер заметки: {index}
        Имя пользователя: {note["username"]}
        Заголовок: {note["title"]}
        Описание заметки: {note["content"]}
        Статус: {note["status"]}
        Дата создания: {note["created_date"]}
        Дедлайн: {note["issue_date"]}
        """)
        print("_" * 80)  # str * int


def date_format():
    for i in range(len(notes)):
        date_ = datetime.strptime(notes[i]['created_date'], "%d-%m-%Y").date()
        notes[i]['created_date'] = date_

# Функция для перевода даты создания из типа datetime в строку
def date_str():
    for i in range(len(notes)):
        str_date = datetime.strftime(notes[i]['created_date'], "%d-%m-%Y")
        notes[i]['created_date'] = str_date


# Функция проверки существования списка
def display_notes(notes, page_number=0):
    if len(notes) == 0:
        print("Список заметок пуст")
    else:
        display_page(notes, page_number)

if __name__ == '__main__':
    notes = [
        {"username": "Дима", "title": "Покупка", "content": "Запчасти для авто", "status": "новая",
         "created_date": "01-02-2025", "issue_date": "01-02-2025"},
        {"username": "Миша", "title": "Тренировка", "content": "Запись в спортзал", "status": "в процессе",
         "created_date": "15-01-2025", "issue_date": "31-01-2025"},
        {"username": "Маша", "title": "Учеба", "content": "Сдача сессии", "status": "в процессе",
         "created_date": "10-01-2025", "issue_date": "10-02-2025"},
        {"username": "Кристина", "title": "Уборка", "content": "Порядок в комнате", "status": "новая",
         "created_date": "01-02-2025", "issue_date": "02-02-2025"},
        {"username": "Катя", "title": "Учеба", "content": "Обучение с репетитором", "status": "выполнено",
         "created_date": "25-01-2025", "issue_date": "27-01-2025"},
        {"username": "Максим", "title": "Ремонт авто", "content": "Запись на СТО", "status": "выполнено",
         "created_date": "25-01-2025", "issue_date": "26-01-2025"},
        {"username": "Сергей", "title": "Ремонт", "content": "Ремонт аппаратуры", "status": "в процессе",
         "created_date": "30-01-2025", "issue_date": "02-02-2025"},
        {"username": "Дима", "title": "Тренировка", "content": "Запись в бассейн", "status": "новая",
         "created_date": "31-01-2025", "issue_date": "31-01-2025"},
        {"username": "Света", "title": "Здоровье", "content": "Запись к врачу", "status": "новая",
         "created_date": "04-02-2025", "issue_date": "04-02-2025"},
        {"username": "Костя", "title": "Работа", "content": "Сдача отчета", "status": "в процессе",
         "created_date": "20-01-2025", "issue_date": "31-01-2025"},

    ]
    #notes = []
    #for i in range(len(notes)):
    #    date_ = datetime.strptime(notes[i]['created_date'], "%d-%m-%Y").date()
    #    notes[i]['created_date'] = date_

    date_format()

    notes = sorted(notes, key=sort_note)

    date_str()
    #for i in range(len(notes)):
    #    str_date = datetime.strftime(notes[i]['created_date'], "%d-%m-%Y")
    #    notes[i]['created_date'] = str_date

    display_notes(notes=notes, page_number=1)