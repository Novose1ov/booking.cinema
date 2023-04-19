import os
import pandas as pd


df = pd.read_csv('data_films.csv')


FILMS = []

choose_film = str()


class Film:
    def __init__(self, name:str, style:str, period:str, start_time:str, hall:str):
        self.name = name
        self.style = style
        self.period = period
        self.start_time = start_time
        self.hall = hall

    def add_to_database(self):
        FILMS.append(self.name)

    def displayFilms(FILMS):
        if FILMS:
            count = 0
            while True:
                key = input("Введите букву: ")
                if key == 'q':
                    choose_film = FILMS[count % (len(FILMS)) - 1]
                    print(choose_film)
                    break
                for i in range(len(FILMS)):
                    if (key) and (count % (len(FILMS)) == i):
                        os.system('CLS')
                        print(FILMS[count % (len(FILMS))])
                        key = ''
                count += 1


film1 = Film("Джон Уик", "Боевик", "110 мин.", "13:00", "VIP")
film2 = Film("Турбо", "мелодрама", "150 мин.", "19:00", "Обычный")
film3 = Film("Человек-павук", "комиксы", "120 мин.", "20:00", "Средний")
film4 = Film("Соник", "комедия", "110 мин.", "13:30", "VIP")
film5 = Film("Фиксики", "Драма", "90 мин.", "16:40", "Большой")

Film.add_to_database(film1)
Film.add_to_database(film2)
Film.add_to_database(film3)
Film.add_to_database(film4)
Film.add_to_database(film5)
