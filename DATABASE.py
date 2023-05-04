import random
import utilits

class Film:
    def __init__(self, name:str, style:str, period:int):
        self.name = name
        self.style = style
        self.period = period


class User:
    def __init__(self, login:str, password:str):
        self.login = login
        self.password = password


class Hall:
    def __init__(self, name:str, num_of_rows:int, num_of_seats_in_row:int):
        self.name = name
        self.num_of_rows = num_of_rows
        self.num_of_seats_in_row = num_of_seats_in_row

"""
class Cinema_post():
    def __init__(self, num_of_date:int, count_films:int):
        self.num_of_date = num_of_date
        self.count_films = count_films
        self.date = ''
        if num_of_date == 0:
            self.date = '28.04'
        elif num_of_date == 1:
            self.date = '29.04'
        elif num_of_date == 2:
            self.date = '30.04'
        else:
            print('404 ERROR в CINEMA_POST CLASS')

        self.films_in_date = []
        self.halls_in_date = []

        for i in range(count_films):
            self.films_in_date.append(random.choice(films_list))
        for k in range(count_films):
            self.halls_in_date.append(random.choice(halls_list))
"""



films_list = list()
users_list = list()
halls_list = list()
dates = ['28.04', '29.04', '30.04']

#синема пост не трогать в csv
cinema_post_list = list()

films_for_28 = {'Соник':'Средний',
                'Москва слезам не верит':'VIP',
                'Шрэк 2':'Средний',
                'Аватар':'Малый',
                'Белый клык':'Малый'}

films_for_29 = {'Фиксики':'VIP',
                'Почему он':'Средний',
                'Убийство в Париже':'VIP',
                'Достать ножи':'Малый',
                'Шрэк 2':'Средний'}

films_for_30 = {'Достать ножи':'Малый',
                'Аватар':'Средний',
                'Белый клык':'Малый',
                'Шрэк 2':'VIP',
                'Фиксики':'VIP'}

cinema_post_list.append(films_for_28)
cinema_post_list.append(films_for_29)
cinema_post_list.append(films_for_30)


# добавление из таблицы
data_film1 = Film('Соник', 'Мультфильм', '140')
data_film2 = Film('Фиксики', 'Фантастика', '120')
data_film3 = Film('Почему он', 'Мелодрама', '125')
data_film4 = Film('Аватар', 'Фантастика', '135')
data_film5 = Film('Шрэк 2', 'Мультфильм', '110')
data_film6 = Film('Убийство в Париже', 'Детектив', '145')
data_film7 = Film('Любовь и голуби', 'Драма', '115')
data_film8 = Film('Москва слезам не верит', 'Комедия', '120')
data_film9 = Film('Достать ножи', 'Ужасы', '130')
data_film10 = Film('Белый клык', 'Приключения', '125')


data_hall1 = Hall('VIP', '3', '4')
data_hall2 = Hall('Малый', '4', '5')
data_hall3 = Hall('Средний', '5', '6')



films_list.append(data_film1)
films_list.append(data_film2)
films_list.append(data_film3)
films_list.append(data_film4)
films_list.append(data_film5)
films_list.append(data_film6)
films_list.append(data_film7)
films_list.append(data_film8)
films_list.append(data_film9)
films_list.append(data_film10)



halls_list.append(data_hall1)
halls_list.append(data_hall2)
halls_list.append(data_hall3)



### FOR USER ###

films = []
for obj_flm in films_list:
    films.append(obj_flm.name)

film_tiles = [utilits.Tile(flm) for flm in films]
date_tiles = [utilits.Tile(date) for date in dates]

### FOR USER ###

