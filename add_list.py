# Запрос информации у пользователя

username_fam = input('Введите фамилию пользователя: ')
username = input("Введите имя пользователя: ")
surname = input("Введите отчество пользователя: ")
#title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'ХХ-ХХ-ХХХХ': ")
issue_date = input("Введите дату истечения заметки в формате 'ХХ-ХХ-ХХХХ': ")

# Если пользователь ввел Имя и отчество с маленькой буквы перевыедем их в большие
#username_new = username.upper()
#surname_new = surname.upper()

# Создаем список заголовков заметки
titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)

# Вывод введенных данных
print("\nВы ввели следующие данные:")
#print(username_fam + ' ' + username_new[0:1] + '.' + surname_new[0:1] + '.')
print(username_fam.title() + ' ' + username.title()[0:1] + '.' + surname.title()[0:1] + '.')
#print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Описание заметки:", content.capitalize())
print("Статус заметки:", status)
print("Дата создания заметки:", created_date[0:5])
print("Дата истечения заметки:", issue_date[0:5])

