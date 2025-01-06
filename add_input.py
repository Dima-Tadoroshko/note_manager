# Запрос информации у пользователя

username_fam = input('Введите фамилию пользователя: ')
username = input("Введите имя пользователя: ")
surname = input("Введите отчество пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'ХХ-ХХ-ХХХХ': ")
issue_date = input("Введите дату истечения заметки в формате 'ХХ-ХХ-ХХХХ': ")

# Запрос нескольких заголовков и добавляем их в список
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
titles = (title1, title2, title3)
# Если пользователь ввел Имя и отчество с маленькой буквы перевыедем их в большие
username_new = username.upper()
surname_new = surname.upper()

# Вывод введенных данных
print("\nВы ввели следующие данные:")
print(username_fam + ' ' + username_new[0:1] + '.' + surname_new[0:1] + '.')
#print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date[0:5])
print("Дата истечения заметки:", issue_date[0:5])