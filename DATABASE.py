import random

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


class Cinema_post():
    def __init__(self, num_of_date:int, count_films:int):
        self.num_of_date = num_of_date
        self.count_films = count_films
        self.date = ''
        if num_of_date == 1:
            self.date = '29.04'
        elif num_of_date == 2:
            self.date = '30.04'
        elif num_of_date == 0:
            self.date = '28.04'
        else:
            print('404 ERROR в CINEMA_POST CLASS')

        self.films_in_date = []
        self.halls_in_date = []

        for i in range(count_films):
            self.films_in_date.append(random.choice(films_list))
        for k in range(count_films):
            self.halls_in_date.append(random.choice(halls_list))




films_list = list()
users_list = list()
halls_list = list()

#синема пост не трогать в csv
cinema_post_list = list()



# добавление из таблицы
data_film1 = Film('Соник', 'Мультфильм', '140')
data_film2 = Film('Фиксики', 'Фантастика', '120')

data_hall1 = Hall('Малый', '4', '5')
data_hall2 = Hall('Средний',  '5', '6')


films_list.append(data_film1)
films_list.append(data_film2)
halls_list.append(data_hall1)
halls_list.append(data_hall2)






