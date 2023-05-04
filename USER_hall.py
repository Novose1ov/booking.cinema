import USER_utilits
import DATABASE

matr = []

class Seat():
    def __init__(self):
        self.is_taking = False
        self.sign = None

        if self.is_taking == False:
            self.sign = '[]'

        elif self.is_taking == True:
            self.sign = '//'


def name_hall(n, m): #создаем список списков, в котором рандомно заняты/свободны места
    global matr
    matrix = matr
    for i in range(n): #СТРОКИ
        row = []
        for j in range(m): #СТОЛБЦЫ
            obj = Seat()
            row.append(obj.sign)
        matrix.append(row)

    matr = matrix
    return matr

def number_hall(H):

    if H == 'VIP':
        n = DATABASE.data_hall1.num_of_rows
        m = DATABASE.data_hall1.num_of_seats_in_row
        name_hall(n,m)
        list_tiles1 = []
        for rows in matr:
            for colums in rows:
                list_tiles1.append(str(colums))
        list_tiles = [utilits.Tile(element_list_tiles1) for element_list_tiles1 in list_tiles1] #делаем из двумерного массива список
        return list_tiles, m

    elif H == 'Малый':
        n = DATABASE.data_hall2.num_of_rows
        m = DATABASE.data_hall2.num_of_seats_in_row
        name_hall(n, m)
        list_tiles1 = []
        for rows in matr:
            for colums in rows:
                list_tiles1.append(str(colums))
        list_tiles = [utilits.Tile(element_list_tiles1) for element_list_tiles1 in list_tiles1]
        return list_tiles, m

    elif H == 'Большой':
        n = DATABASE.data_hall3.num_of_rows
        m = DATABASE.data_hall2.num_of_seats_in_row
        name_hall(n, m)
        list_tiles1 = []
        new_list = []
        for rows in matr:
            for colums in rows:
                list_tiles1.append(str(colums))
        list_tiles = [utilits.Tile(element_list_tiles1) for element_list_tiles1 in list_tiles1]
        return list_tiles, m

