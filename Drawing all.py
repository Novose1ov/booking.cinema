import os


class headline():
    def __init__(self):
        pass

    def create_headline(self, COLS:int, HEAD:str):
        self.COLS = COLS
        self.HEAD = HEAD
        SPACE_before = int( (COLS + 1 - len(HEAD)) / 2)
        SPACE_after = int(COLS + 1 - SPACE_before - len(HEAD))
        return (SPACE_before*'\033[44m\033[37m\033[1m ') + (HEAD) + (SPACE_after*' ') + ('\033[0m\n')


class authors():
    def __init__(self):
        pass

    def create_authors(self, SPACE:int, COLS:int, admins:tuple):
        self.SPACE = SPACE
        self.COLS = COLS
        self.admins = admins
        s = ''
        for name in admins:
            s += (name + SPACE*' ')
        space_before = int( (COLS + 1 - len(s)) / 2)
        space_after = int(COLS + 1 - space_before - len(s))
        return ('\033[44m\033[37m\033[1m '*space_before) + (s) + (' '*space_after) + ('\033[0m')


class tab():
    def __init__(self):
        pass

    def create_tab(self, COLS:int, SPACE:int, TAB:tuple, num:int) -> str:
        self.COLS = COLS
        self.SPACE = SPACE
        self.TAB = TAB
        self.num = num
        st = str()
        LenTab = 0

        for i in TAB:
            LenTab += len(i)

        for ind, tab in enumerate(TAB):
            if ind == num:
                st += ('\033[30m\033[1m\033[47m') + (' ' * int(SPACE / 2)) + tab + (' ' * int(SPACE / 2))
            else:
                st += ('\033[37m\033[1m\033[44m') + (' ' * int(SPACE / 2)) + tab + (' ' * int(SPACE / 2))

        return ('\033[1m\033[37m\033[44m') + (' ' * int(SPACE / 2)) + ('\033[0m') + \
                (st) + ('\033[1m\033[37m\033[44m') + \
                 (' '*int(COLS + 1 - (int(SPACE / 2)+(LenTab)+(len(TAB)*SPACE)))) + ('\033[0m') + ('\n')


class table():
    def __init__(self):
        pass

    def create_table(self, COLS: int, ROWS: int, num:int):
        self.COLS = COLS
        self.ROWS = ROWS
        self.num = num
        plot = ''


        for row in range(ROWS):
            for col in range(COLS+1):

                if (row == 0) and (col == 0):
                    plot += '\033[47m\033[34m'
                    plot += '┏'
                if (row == 0) and (col == COLS):
                    plot += '┓'
                if (row == ROWS-1) and (col == 0):
                    plot += '┗'
                if (row == ROWS-1) and (col == COLS):
                    plot += '┛\033[44m\033[37m'


                if (row == 0 or row == ROWS-1) and (0 < col < COLS):
                    plot += '━'
                if (0 < row < ROWS-1) and (col == 0 or col == COLS):
                    plot += '┃'

                # 2-нижняя граница, 2-рамка, 2-отступ сверху/снизу, 6=макс.высота.функц.+1
                # 4 - левая граница, 2 - рамка, 2 - пробелы, 12+1 - макс.длина, 2 - пробел+стрелочка

                if (0 < row < MAX_HEIGHT_FUNC + 7) and (0 < col < MAX_HEIGHT_FUNC + 13):
                    if 0 < col < 5 and 2 < row < 12:
                        plot += ' '
                    if col == 5 and row == 3:
                        plot += '┏'
                    if col == 5  and 3 < row < 11:
                        plot += '┃'
                    if col == 5 and row == 11:
                        plot += '┗'
                    if (row == 3 or row == 11) and (4 < col < 25):
                        plot += '━'
                    if (5 < col < 8) and (3< row <1):
                        plot += ' '

                    #if col < 5 and 4 < row < MAX_HEIGHT_FUNC + 5:
                    #    plot += ' '

                #if (0 < row < ROWS-1) and (col <= 4 and col >= 4):
                #    plot += ' '


                if col == COLS:
                    plot += '\n'
        return plot



COLS = 155
ROWS = 43
SPACE = 4
HEADSTROKE = 'ADMINISTRATOR SETUP MODE'
TABS = ('Main', 'Edit', 'Movie_Poster', 'Exit')
AUTHORS = ('Читаева Анастасия', 'Чучунова Юлия', 'Добрева Валентина', \
            'Тишкин Алексей', 'Праведников Илья', 'Новоселов Данил')

FUNCTIONS = (('Users', 'Films', 'Halls'),
             ('Add Film', 'Remove Film', ' ', 'Add Hall', 'Remove Hall'),
             ('Movie Poster', 'Edit'),
             ('Exit'))

MAX_LEN_FUNC = 0
MAX_HEIGHT_FUNC = 0
for i in FUNCTIONS:
    for k in i:
        if len(k) > MAX_LEN_FUNC:
            MAX_LEN_FUNC = len(k)
    if len(i) > MAX_HEIGHT_FUNC:
        MAX_HEIGHT_FUNC = len(i)

count = 0
key = None

Headline = headline()
Tab = tab()
Table = table()
Authors = authors()
plot = str()

def choose_menu(plot, num):
    objects = (Headline.create_headline(COLS, HEADSTROKE), \
               Tab.create_tab(COLS, SPACE, TABS, num), \
               Table.create_table(COLS, ROWS, num), \
               Authors.create_authors(SPACE, COLS, AUTHORS))
    for object in objects:
        plot += object
    return plot

while True:
    for index in range(len(TABS)):
        if index == count%len(TABS):
            os.system("CLS")
            print(choose_menu(plot, count%len(TABS)))
            key = input('')
    if key == ' ':
        input()
    count += 1
