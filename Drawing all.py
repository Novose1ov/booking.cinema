import os
os.system('CLS')

COLS = 155
ROWS = 45

class admin_plot():

    def __init__(self, COLS:int, ROWS:int):
        self.COLS = COLS
        self.ROWS = ROWS

        self.plot = str()
        self.HEAD = 'ADMINISTRATOR SETUP MODE'
        self.SPACE = 4
        self.TABS = ('Main', 'Edit', 'Movie_Poster', 'Exit')


        for row in range(ROWS + 1):
            for col in range(COLS + 1):
                if (row == 0):
                    SPACE_before = int((COLS + 1 - len(self.HEAD)) / 2)
                    SPACE_after = int(COLS + 1 - SPACE_before - len(self.HEAD))
                    self.plot += (SPACE_before * '\033[44m\033[37m\033[1m ') + (self.HEAD) + (SPACE_after * ' ') + ('\n')
                    break
                if (row == 1):
                    st = str()
                    for tab in self.TABS:
                        st += (' ' * self.SPACE) + tab
                    self.plot += st + ' ' * int(COLS+1 - len(st)) + ('\033[0m')
                    break

                if (row == 3) and (col == 0):
                    self.plot += '\033[47m\033[34m'
                    self.plot += '┏'
                if (row == 3) and (col == COLS):
                    self.plot += '┓'
                if (row == ROWS-1) and (col == 0):
                    self.plot += '┗'
                if (row == ROWS-1) and (col == COLS):
                    self.plot += '┛\033[44m\033[37m'

                if (row == 3 or row == ROWS-1) and (0 < col < COLS):
                    self.plot += '━'
                if (3 < row < ROWS-1) and (col == 0 or col == COLS):
                    self.plot += '┃'

                if (3 < row < ROWS-1) and (0 < col < COLS):
                    self.plot += ' '
    
                if col == COLS:
                    self.plot += '\n'


                if row == ROWS:
                    admins = (
                    'Читаева Анастасия', 'Чучунова Юлия', 'Добрева Валентина', 'Тишкин Алексей', 'Праведников Илья',
                    'Новоселов Данил')
                    s = ''
                    for name in admins:
                        s += (name + self.SPACE*' ')
                    space_before = int((COLS+1-len(s))/2)
                    space_after = int(COLS + 1 - space_before - len(s))
                    self.plot += ('\033[44m\033[37m\033[1m '*space_before) + (s) + (' '*space_after) + ('\033[0m')
                    break


    def draw(self):
        print(self.plot)



object = admin_plot(COLS, ROWS)
while True:
    os.system('CLS')
    object.draw()
    input()



