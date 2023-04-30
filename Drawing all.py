import os


class headline():
    def __init__(self):
        pass

    def create_headline(self, COLS:int, HEAD:str):
        self.COLS = COLS
        self.HEAD = HEAD
        SPACE_before = int( (COLS + 1 - len(HEAD)) / 2)
        SPACE_after = int(COLS + 1 - SPACE_before - len(HEAD))
        return (SPACE_before*'\033[44m\033[37m\033[1m ') + (HEAD) + (SPACE_after*' ') + ('\n')


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

    def create_tab(self, COLS:int, SPACE:int, TAB:tuple):
        self.COLS = COLS
        self.SPACE = SPACE
        self.TAB = TAB
        st = str()
        for tab in TAB:
            st += (' ' * SPACE) + tab
        return (st) + (' '*int(COLS + 1 - len(st))) + ('\033[0m\n')


class table():
    def __init__(self):
        pass

    def create_table(self, COLS: int, ROWS: int):
        self.COLS = COLS
        self.ROWS = ROWS

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


                if (0 < row < ROWS-1) and (0 < col < COLS):
                    plot += ' '


                if col == COLS:
                    plot += '\n'
        return plot


while True:
    os.system("CLS")

    COLS = 155
    ROWS = 43
    SPACE = 4
    HEADSTROKE = 'ADMINISTRATOR SETUP MODE'
    TABS = ('Main', 'Edit', 'Movie_Poster', 'Exit')
    AUTHORS = ('Читаева Анастасия', 'Чучунова Юлия', 'Добрева Валентина', \
                'Тишкин Алексей', 'Праведников Илья', 'Новоселов Данил')

    Headline = headline()
    Tab = tab()
    Table = table()
    Authors = authors()

    objects = (Headline.create_headline(COLS, HEADSTROKE), \
               Tab.create_tab(COLS, SPACE, TABS), \
               Table.create_table(COLS, ROWS), \
               Authors.create_authors(SPACE, COLS, AUTHORS))

    plot = str()
    for object in objects:
        plot += object

    print(plot, end='')
    input()
