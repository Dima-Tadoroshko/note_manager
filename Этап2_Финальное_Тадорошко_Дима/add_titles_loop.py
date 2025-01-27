titles = []
# Создание списка заголовков
stop = 'стоп' # ввод доп переменный для проверки
# Цикл по вводу пользователем данных и проверка на выход
while True:
    title = input(f"Введите заголовок заметки \n(или введите 'Стоп' для завершения ввода данных):  ")
    title = title.lower().strip()
    if title == stop :
        break
    titles.append(title.capitalize()) # запись элементов в список с заглавной буквы
#print(titles)
# Удаление пустых значений и пробелов
titles = [x for x in titles if x.strip()]
#print(titles)
""" 
проверка на уникальность элементов списка и вывод на экран
Преобразовываем список в набор с помощью функции set(). Затем преобразовываем набор обратно в список и
выводим новый список"""
set_res = set(titles)
list_res = list(set_res)
set_res = list_res.sort()# сортируем список по алфавиту
for item in list_res:
    print(' - ' + item)
