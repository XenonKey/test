import os

def record_users():
    """Функция для добавления записи в файл"""
    n_books = int(input('Введите количество новых пользователей: '))
    file = open('users_info', 'a', encoding='utf-8')

    for book in range(n_books):
        name = input('Введите имя пользователя: ') + '\n'
        email = input('Введите почту пользователя: ') + '\n'
        city = input('Введите город пользователя: ') + '\n'
        file.write(name)
        file.write(email)
        file.write(city)

    file.close()
    print('Запись сохранена' if n_books == 1 else 'Записи сохранены')


def change_city():
    """Функция для изменения города в файле"""
    user_to_edit = input('Введите пользователя для смены города: ') + '\n'
    new_city = input('Введите новый город пользователя: ') + '\n'

    file = open('users_info', 'r', encoding='utf-8')
    new_file = open('new_users_info', 'w', encoding='utf-8')

    user_name = file.readline()
    while user_name != '':
        email = file.readline()
        city = file.readline()
        if user_name == user_to_edit:
            new_file.write(user_name)
            new_file.write(email)
            new_file.write(new_city)
        else:
            new_file.write(user_name)
            new_file.write(email)
            new_file.write(city)
        user_name = file.readline()
    file.close()
    new_file.close()
    os.remove('users_info')
    os.rename('new_users_info', 'users_info')


