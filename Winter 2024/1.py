# считываем данные
N = int(input().strip())

for _ in range(N):
    tinkoff = set('TINKOFF')  # множество букв
    f = 1  # повтор буквы F
    s = input().strip()  # входящая строка
    idx = 0  # индекс текущей буквы в s
    if len(s) != 7:  # если длина не равна 7 - ответ нет
        print('no')
    else:  # иначе
        for idx in range(len(s)):  # проходим по строке и убираем буквы из множества
            if s[idx] in tinkoff:
                tinkoff.remove(s[idx])
            else:   # если буквы нет в множестве и она F - уменьшаем счетчик
                if s[idx] == 'F':
                    f -=1

        if not tinkoff and f < 1:  # если не осталось букв - ответ да
            print('yes')
        else:  # иначе ответ - нет
            print('no')
