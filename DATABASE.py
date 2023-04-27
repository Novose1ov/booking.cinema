class Film:
    def __init__(self, name:str, style:str, period:str):
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

films_list = list()
users_list = list()
halls_list = list()



