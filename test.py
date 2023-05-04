import pandas as pd
from DATABASE import *
from DB.DataBase import Table
import os


# name = 'users'

# table = pd.read_csv(os.path.abspath(f'{name}.csv'), sep=',')
# # for obj in objects:
# print(list(table['log']) == [])
    
# table.to_csv(os.path.abspath(f'{name}.csv'), index=False)

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



for tb in ['films', 'holls', 'users']:
    table = Table(tb).get_collection_by_index()
    for row in table:
        if tb == 'films':
            films_list.append(Film(str(row[1]), str(row[2]), str(row[3])))
        elif tb == 'holls':
            halls_list.append(Hall(str(row[1]), str(row[2]), str(row[3])))
        elif tb == 'users':
            users_list.append(User(str(row[1]), str(row[2])))