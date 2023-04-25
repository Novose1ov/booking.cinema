import os

def first_date():
    return'''
  █████████
  ██28.04██  29.04    30.04
  █████████
'''
def second_date():
    return'''
           █████████
    28.04  ██29.04██  30.04
           █████████
'''
def third_date():
    return'''         
                    █████████
    28.04    29.04  ██30.04██
                    █████████
'''


list = [first_date(), second_date(), third_date()]
count = 0

while True:
    key = input()
    for i in range(len(list)):
        if (count % len(list)) == i:
            os.system('CLS')
            print(list[count % len(list)])
            key = ''
    count += 1

