import os
import utilits
import hall

count = 0
list_tiles = [utilits.Tile('28.04'), utilits.Tile('29.04'), utilits.Tile('30.04')]
list_tiles1 = [utilits.Tile('почему он'), utilits.Tile('аватар'), utilits.Tile('шрэк 2')]
list_tiles2 = [utilits.Tile('убийство в париже'), utilits.Tile('любовь и голуби'), utilits.Tile('москва слезам не верит')]
list_tiles3 = [utilits.Tile('достать ножи'), utilits.Tile('соник'), utilits.Tile('белый клык')]

print ("Нажмите Enter, чтобы переключить. Чтобы выбрать, нажмите пробел")
while True: # вывод на консоль даты
    key = input()
    if key == ' ':
        choose_date = count % len(list_tiles)
        os.system('CLS')
        break
    else:
        utilits.print_tile(list_tiles, count)
    count += 1

print ("Выберете фильм: ")

if choose_date == 1: #28.04, фильмы
    while True:
        key = input()
        if key == ' ':
            choose_movie = count % len(list_tiles1)
            os.system('CLS')
            break
        else:
            utilits.print_tile(list_tiles1, count)
        count += 1

if choose_date == 2: #29.04, фильмы
    while True:
        key = input()
        if key == ' ':
            choose_movie = count % len(list_tiles2)
            os.system('CLS')
            break
        else:
            utilits.print_tile(list_tiles2, count)
        count += 1

if choose_date == 0: #30.04, фильмы
    while True:
        key = input()
        if key == ' ':
            choose_movie = count % len(list_tiles3)
            os.system('CLS')
            break
        else:
            utilits.print_tile(list_tiles3, count)
        count += 1

print ("Выберете место: \n ( [] - место свободно, // - место занято)")

if choose_movie == 1: #зал VIP
    flag = 0
    hall_list = hall.number_hall(1)
    while (flag == 0):
        i = utilits.columns_tile(hall_list, 10)
        if (hall_list[i-1].tile[1][5:-2] == '//'):
            print("Место занято\n Выберете другое место")
            input()
        else:
            print("Вы забронировали место на сеанс. Удачного просмотра!!!")
            input()
            flag = 1

if choose_movie == 2: # зал small
    flag = 0
    hall_list = hall.number_hall(1)
    while (flag == 0):
        i = utilits.columns_tile(hall_list, 9)

        if(hall_list[i- 1].tile[1][5:-2] == '//'):
            print("Место занято\n Выберете другое место")
            input()
        else:
            print("Вы забронировали место на сеанс. Удачного просмотра!!!")
            input()
            flag = 1

if choose_movie == 0: # зал big
    flag = 0
    hall_list = hall.number_hall(1)
    while (flag == 0):
        i = utilits.columns_tile(hall_list, 18)

        if (hall_list[i- 1].tile[1][5:-2] == '//'):
            print("Место занято\n Выберете другое место")
            input()
        else:
            print("Вы забронировали место на сеанс. Удачного просмотра!!!")
            input()
            flag=1
