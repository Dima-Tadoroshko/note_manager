#Создание словоря
notes = {'note1' : "выполнено", 'note2' : "в процессе", 'note3' : "отложено", 'result' : 'в процессе'}
# вывод текущего статуса заметки
print('Статус текущей заметки: ' + notes['note2'])

# Ввод пользовавтелем данных и проверка на корректность
while True:
    choice = input('Выберете текущий статус заметки: ' + '\n 1. ' + notes['note1'] + '\n 2. ' + notes['note2'] +
                   '\n 3. ' + notes['note3'] + '\n Вы можете ввести как цифры, так слово' + '\n Ваш выбор: ')
    if choice == "выполнено" or choice == '1':
        print('Вы выбрали: выполнено')
        break
    elif choice == "в процессе" or choice == '2':
        print('Вы выбрали: в процессе')
        break
    elif choice == "отложено" or choice == '3':
        print('Вы выбрали: отложено')
        break
    else:
        print("Введены не корректные данные")

#print(choice)
# запись результата ввода и проверки в словарь
if choice == "выполнено" or choice == '1':
    notes['result'] = 'выполнено'
elif choice == "в процессе" or choice == '2':
    notes['result'] = 'в процессе'
elif choice == "отложено" or choice == '3':
    notes['result'] = 'отложено'
print('Статус заметки успешно обновлён на: ' + notes['result'])
