import DATABASE, ADMIN_menu_continue, os



class headline():
    def __init__(self):
        pass

    def create_headline(self, COLS:int, HEAD:str):
        self.COLS = COLS
        self.HEAD = HEAD
        SPACE_before = int( (COLS + 1 - len(HEAD)) / 2)
        SPACE_after = int(COLS + 1 - SPACE_before - len(HEAD))
        return (SPACE_before*'\033[44m\033[37m\033[1m ') + (HEAD) + (SPACE_after*' ') + ('\033[0m\n')

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

def start_ADMIN_main():

    hd = headline()
    tb = tab()
    auth = authors()

    TABS = ('Users', 'Films', 'Halls', 'Movie Poster', 'Add Film', 'Add Hall', \
            'Remove Film', 'Remove Hall', 'Edit Movie_Poster', 'Exit')
    AUTHORS = ('Читаева Анастасия', 'Чучунова Юлия', 'Добрева Валентина', \
               'Тишкин Алексей', 'Праведников Илья', 'Новоселов Данил')


    count = 0
    key = None
    while True:
        for index in range(len(TABS)):
            if index == count % len(TABS):
                os.system('CLS')
                print(hd.create_headline(155, 'ADMINISTRATOR SETUP MODE'), end='')
                print(tb.create_tab(155, 4, TABS, count%len(TABS)), end = '')
                print('\033[47m\033[34m' + '┏' + '━'*154 + '┓')
                print('┃' + ' '*154 +'┃')
                print('┃    ┏━━━━━━━━━━━━━━━━━━━━━━━┓'+125*' '+'┃')
                print('┃    ┃ Переключиться [Enter] ┃'+125*' '+'┃')
                print('┃    ┃ Выбрать       [Space] ┃'+125*' '+'┃')
                print('┃    ┗━━━━━━━━━━━━━━━━━━━━━━━┛' + 125 * ' ' + '┃')
                key=input("""┃                                                                                                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")


        count += 1

        if key == ' ':
            if count % len(TABS) == 0:
                input('Приходите ещё!')
                break
            else:
                menu_continue.contTinue(str((count) % len(TABS)))
                continue
        # функция обновления списков из DataBase в csv формат