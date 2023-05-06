import os
import USER_utilits
import USER_hall
import DATABASE



class User:
    def __init__(self):
        self.choose_date = 0
        self.choose_movie = 0


    def choosing_date(self):
        count = 0
        while True:  # вывод на консоль даты
            USER_utilits.print_tile(DATABASE.date_tiles, count)
            key = input()

            if key == ' ':
                choose_date = count % len(DATABASE.date_tiles)
                os.system('CLS')
                return (choose_date)
            count += 1


    def choose_film(self, choose_date:int):
        flms_f_28 = [USER_utilits.Tile(i) for i in DATABASE.films_for_28]
        flms_f_29 = [USER_utilits.Tile(i) for i in DATABASE.films_for_29]
        flms_f_30 = [USER_utilits.Tile(i) for i in DATABASE.films_for_30]

        count = 0
        if choose_date == 0:  # 28.04, фильмы
            while True:
                USER_utilits.print_tile(flms_f_28, count)
                key = input()

                if key == ' ':
                    choose_movie = count % len(flms_f_28)
                    os.system('CLS')
                    return (choose_movie)
                count += 1


        elif choose_date == 1: #29.04, фильмы
            while True:
                USER_utilits.print_tile(flms_f_29, count)
                key = input()

                if key == ' ':
                    choose_movie = count % len(flms_f_29)
                    os.system('CLS')
                    return (choose_movie)
                count += 1


        elif choose_date == 2: #30.04, фильмы
            while True:
                USER_utilits.print_tile(flms_f_30, count)
                key = input()

                if key == ' ':
                    choose_movie = count % len(flms_f_30)
                    os.system('CLS')
                    return (choose_movie)
                count += 1


    def choosing_seat(self, choose_date:int, choose_movie:int):
        L = [DATABASE.films_for_28, DATABASE.films_for_29, DATABASE.films_for_30][choose_date]

        count = 0
        for i in L:
            if count == choose_movie:
                H = L[i]
            count += 1


        if H == 'VIP': #зал VIP
            flag = 0
            hall_list, m = USER_hall.number_hall(H)
            while (flag == 0):
                i, ost = USER_utilits.columns_tile(hall_list, m)

                if (hall_list[i-1].tile[1][5:-2] == '//'):
                    input("Место занято\n Выберете другое место")
                else:
                    input("Вы забронировали место на сеанс. Удачного просмотра!!!")
                    USER_hall.matr[0][ost-1].is_taking == True


        elif H == 'Малый': # зал small
            flag = 0
            hall_list, m = USER_hall.number_hall(H)
            while (flag == 0):
                i, ost = USER_utilits.columns_tile(hall_list, m)

                if(hall_list[i-1].tile[1][5:-2] == '//'):
                    input("Место занято\n Выберете другое место")
                else:
                    input("Вы забронировали место на сеанс. Удачного просмотра!!!")
                    USER_hall.matr[0][ost-1].is_taking == True


        elif H == 'Большой': # зал big
            flag = 0
            hall_list, m = USER_hall.number_hall(H)

            while (flag == 0):
                i, ost = USER_utilits.columns_tile(hall_list, m)

                if (hall_list[i-1].tile[1][5:-2] == '//'):
                    input("Место занято\n Выберете другое место")
                else:
                    input("Вы забронировали место на сеанс. Удачного просмотра!!!")
                    USER_hall.matr[0][ost-1].is_taking == True





def start_USER_main():
    user1 = User()
    ch_date = user1.choosing_date()
    ch_movie = user1.choose_film(ch_date)
    user1.choosing_seat(ch_date, ch_movie)


