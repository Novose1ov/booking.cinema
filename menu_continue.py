import DATABASE
import random

def contTinue(choice):


    # Вывести БД с пользователями
    if choice == '1':
        if len(DATABASE.users_list) > 0:
            for index, user in enumerate(DATABASE.users_list):

                max_len_stroke = int(len(user.login + user.password))

                if len(DATABASE.users_list) == 1:
                    print('+' + '-' * (max_len_stroke + 5) + '+')
                    print('|' + ' ' + user.login + ' ', end='')
                    print('|' + ' ' + user.password + ' ' + '|')

                elif len(DATABASE.users_list) > 1:
                    print('+' + '-' * (max_len_stroke + 5) + '+')
                    print('|' + ' ' + user.login + ' ', end='')
                    print('|' + ' ' + user.password + ' ' + '|')

            print('+' + '-' * (max_len_stroke + 5) + '+')
            input()
        else:
            input('\nБаза данных пуста.')


    # Вывести БД с фильмами
    elif choice == '2':
        if len(DATABASE.films_list) > 0:
            for index, film in enumerate(DATABASE.films_list):

                max_len_stroke = int(len(film.name + film.style + film.period))

                if len(DATABASE.films_list) == 1:
                    print('+' + '-' * (max_len_stroke + 8) + '+')
                    print('|' + ' ' + film.name + ' ', end='')
                    print('|' + ' ' + film.style + ' ', end='')
                    print('|' + ' ' + film.period + ' ' + '|')

                elif len(DATABASE.films_list) > 1:
                    print('+' + '-' * (max_len_stroke + 8) + '+')
                    print('|' + ' ' + film.name + ' ', end='')
                    print('|' + ' ' + film.style + ' ', end='')
                    print('|' + ' ' + film.period + ' ' + '|')

            print('+' + '-' * (max_len_stroke + 8) + '+')
            input()
        else:
            input('\nБаза данных пуста.')


    # Вывести БД с залами
    elif choice == '3':
        if len(DATABASE.halls_list) > 0:
            for index, hall in enumerate(DATABASE.halls_list):

                max_len_stroke = int(len(hall.name + hall.num_of_rows + hall.num_of_seats_in_row))

                if len(DATABASE.halls_list) == 1:
                    print('+' + '-' * (max_len_stroke + 8) + '+')
                    print('|' + ' ' + hall.name + ' ', end='')
                    print('|' + ' ' + hall.num_of_rows + ' ', end='')
                    print('|' + ' ' + hall.num_of_seats_in_row + ' ' + '|')

                elif len(DATABASE.films_list) > 1:
                    print('+' + '-' * (max_len_stroke + 8) + '+')
                    print('|' + ' ' + hall.name + ' ', end='')
                    print('|' + ' ' + hall.num_of_rows + ' ', end='')
                    print('|' + ' ' + hall.num_of_seats_in_row + ' ' + '|')

            print('+' + '-' * (max_len_stroke + 8) + '+')
            input()
        else:
            input('\nБаза данных пуста.')


    # Вывести Киноафишу
    elif choice == '4':
        num_of_date = 0
        for i in range(3):
            day_object = DATABASE.Cinema_post(num_of_date, random.randint(1, 3))
            DATABASE.cinema_post_list.append(day_object)

        for object_day in DATABASE.cinema_post_list:
            print(f'{object_day.date}')
            for index, film in enumerate(object_day.films_in_date):
                print(f' {film.name} | {object_day.halls_in_date[index].name}')


    # Добавить фильм в БД
    elif choice == '5':
        add_name_film = input('\nДобавьте название фильма: ')
        add_style_film = input('Добавьте жанр фильма: ')
        add_period_film = input('Добавьте длительность фильма:  ')

        film_object = DATABASE.Film(add_name_film, add_style_film, add_period_film)
        DATABASE.films_list.append(film_object)


    # Добавить кинозал в БД
    elif choice == '6':
        add_name_hall = input('\nДобавьте название зала: ')
        add_num_of_rows_hall = input('Добавьте кол-во рядов: ')
        add_num_of_seats_in_row_hall = input('Добавьте кол-во мест в ряду: ')

        hall_object = DATABASE.Hall(add_name_hall, add_num_of_rows_hall, add_num_of_seats_in_row_hall)
        DATABASE.halls_list.append(hall_object)


    # Удалить фильм из БД
    elif choice == '7':
        if len(DATABASE.films_list) > 0:
            for object_film in DATABASE.films_list:
                if object_film.name == input('Какой фильм нужно удалить? '):
                    DATABASE.films_list.remove(object_film)
                else:
                    input('Данного фильма нет в базе данных.')
        else:
            input('Данного фильма нет в базе данных.')


    # Удалить кинозал из БД
    elif choice == '8':
        if len(DATABASE.halls_list) > 0:
            for object_hall in DATABASE.halls_list:
                if object_hall.name == input('Какой зал нужно удалить? '):
                    DATABASE.halls_list.remove(object_hall)
                else:
                    input('Данного зала нет в базе данных.')
        else:
            input('Данного зала нет в базе данных.')


    # Редактировать Киноафишу
    elif choice == '9':
        pass