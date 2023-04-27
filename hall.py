import  utilits
import random

matr = []

def name_hall(n, m): #создаем список списков, в котором рандомно заняты/свободны места
    global matr
    matrix = matr
    for i in range(n): #СТРОКИ
        row = []
        for j in range(m): #СТОЛБЦЫ
            row.append(random.randint(0, 1))
        matrix.append(row)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                matrix[i][j] = "//" # место занято
            else:
                matrix[i][j] = "[]" # место свободно
    matr = matrix
    return matr

def number_hall(choose_movie):
    if choose_movie == 1:
        n = 10
        m = 10
        name_hall(n,m)
        list_tiles1 = []
        for rows in matr:
            for colums in rows:
                list_tiles1.append(str(colums))
        list_tiles = [utilits.Tile(element_list_tiles1) for element_list_tiles1 in list_tiles1] #елаем из двумерного массива список
        return list_tiles

    if choose_movie == 2:
        n = 8
        m = 9
        name_hall(n, m)
        list_tiles1 = []
        for rows in matr:
            for colums in rows:
                list_tiles1.append(str(colums))
        list_tiles = [utilits.Tile(element_list_tiles1) for element_list_tiles1 in list_tiles1]
        return list_tiles

    if choose_movie == 0:
        count = 0
        n = 20
        m = 18
        name_hall(n, m)
        list_tiles1 = []
        new_list = []
        for rows in matr:
            for colums in rows:
                list_tiles1.append(str(colums))
        list_tiles = [utilits.Tile(element_list_tiles1) for element_list_tiles1 in list_tiles1]
        return list_tiles

