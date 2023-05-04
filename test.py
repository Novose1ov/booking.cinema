import DATABASE

"""
films_for_30 = {'Достать ножи':'Малый',
                'Аватар':'Средний',
                'Белый клык':'Малый',
                'Шрэк 2':'VIP',
                'Фиксики':'VIP'}

# по ключам
for i in films_for_30:
    print(i)

# по значениям
for i in films_for_30:
    print(films_for_30[i])

print(films_for_30['Достать ножи'])

"""

choose_date = 1
choose_movie = 4






L = [DATABASE.films_for_28, DATABASE.films_for_29, DATABASE.films_for_30][choose_date]
count = 0
for i in L:
    if count == choose_movie:
        print(L[i])
    count += 1
