
    count = 0
    key = None
    while True:
        for index in range(len(lst)):
            if index == count % len(lst):
                os.system('CLS')
                print(lst[count % len(lst)])
                key = input('Введи: ')
        count += 1
        if key == 'y':
            print(count % len(lst))
            if count % len(lst) == 0:
                input('Приходите ещё!')
                break
            else:
                menu_continue.contTinue(str((count) % len(lst)))
                continue