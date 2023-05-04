import os
import DATABASE
from ADMIN_main import start_ADMIN_main
from USER_main import start_USER_main
######################################################################################################
while True:
    os.system('CLS')
    print('Welcome!')
    input('Нажмите Enter, чтобы продолжить...')

    os.system('CLS')
    l = input('Login: ')
    p = input('Password: ')

    if l == '':
        input('Неккоректный ввод логина')
    elif p == '':
        input('Неккоректный ввод пароля')
    elif l == '' and p == '':
        input('Неккоректный ввод логина и пароля')
    elif l == 'admin' and p == 'admin':
        start_ADMIN_main()
    else:
        user_object = DATABASE.User(l, p)
        DATABASE.users_list.append(user_object)
        start_USER_main()
######################################################################################################




