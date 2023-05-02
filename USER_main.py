import os
import utilits
import hall

list_tiles = [utilits.Tile('28.04'), utilits.Tile('29.04'), utilits.Tile('30.04')]
list_tiles1 = [utilits.Tile('почему он'), utilits.Tile('аватар'), utilits.Tile('шрэк 2')]
list_tiles2 = [utilits.Tile('убийство в париже'), utilits.Tile('любовь и голуби'), utilits.Tile('москва слезам не верит')]
list_tiles3 = [utilits.Tile('достать ножи'), utilits.Tile('соник'), utilits.Tile('белый клык')]

class User:
    def __init__(self):
        self.choose_date = 0
        self.choose_movie = 0

    def choosing_date(self):
        count = 0
        print("Нажмите Enter, чтобы переключить. Чтобы выбрать, нажмите пробел")
        while True:  # вывод на консоль даты
            key = input()
            if key == ' ':
                choose_date = count % len(list_tiles)
                os.system('CLS')
                break
            else:
                utilits.print_tile(list_tiles, count)
            count += 1
        return choose_date

    def choose_film(self, choose_date : int):
        count = 0
        print("Выберете фильм: ")

        if choose_date == 1:  # 28.04, фильмы
            while True:
                key = input()
                if key == ' ':
                    choose_movie = count % len(list_tiles1)
                    os.system('CLS')
                    break
                else:
                    utilits.print_tile(list_tiles1, count)
                count += 1
            return choose_movie

        elif choose_date == 2: #29.04, фильмы
            while True:
                key = input()
                if key == ' ':
                    choose_movie = count % len(list_tiles2)
                    os.system('CLS')
                    break
                else:
                    utilits.print_tile(list_tiles2, count)
                count += 1

            return choose_movie
        elif choose_date == 0: #30.04, фильмы
            while True:
                key = input()
                if key == ' ':
                    choose_movie = count % len(list_tiles3)
                    os.system('CLS')
                    break
                else:
                    utilits.print_tile(list_tiles3, count)
                count += 1
            return choose_movie

    def choosing_seat(self, choose_movie:int):
        count = 0
        print ("Выберете место: \n ( [] - место свободно, // - место занято)")

        if choose_movie == 1: #зал VIP
            flag = 0
            hall_list, m = hall.number_hall(choose_movie)
            while (flag == 0):
                i, ost = utilits.columns_tile(hall_list, m)
                if (hall_list[i-1].tile[1][5:-2] == '//'):
                    input("Место занято\n Выберете другое место")
                else:
                    input("Вы забронировали место на сеанс. Удачного просмотра!!!")
                    hall.matr[ost].is_taking == True

        elif choose_movie == 2: # зал small
            flag = 0
            hall_list, m = hall.number_hall(choose_movie)
            while (flag == 0):
                i, ost = utilits.columns_tile(hall_list, m)

                if(hall_list[i- 1].tile[1][5:-2] == '//'):
                    input("Место занято\n Выберете другое место")
                else:
                    input("Вы забронировали место на сеанс. Удачного просмотра!!!")
                    hall.matr[ost].is_taking == True

        elif choose_movie == 0: # зал big
            flag = 0
            hall_list, m = hall.number_hall(choose_movie)
            while (flag == 0):
                i, ost = utilits.columns_tile(hall_list, m)

                if (hall_list[i- 1].tile[1][5:-2] == '//'):
                    input("Место занято\n Выберете другое место")
                else:
                    input("Вы забронировали место на сеанс. Удачного просмотра!!!")
                    hall.matr[ost].is_taking == True

user1 = User()
ch_date = user1.choosing_date()
ch_movie = user1.choose_film(ch_date)
user1.choosing_seat(ch_movie)