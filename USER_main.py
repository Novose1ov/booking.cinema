import os
from main import Film, FILMS

def printWELCOME():
    print("Добро пожаловать в кинотеатр!")


def print_choose_DATE():
    print("Выбери дату:", )

def displayFilms():
    Film.displayFilms(FILMS)


printWELCOME()
print_choose_DATE()
displayFilms()






