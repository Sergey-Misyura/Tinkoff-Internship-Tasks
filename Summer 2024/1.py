# считываем данные
m = int(input().strip())  # количество дней
seq = list(map(int, input().split()))  # список оценок

answer = -1  # ответ
if len(seq) < 7:  # если нет 7 дней - выводим ответ
    print(answer)
else:
    bad_count = 0  # количество плохих оценок
    good_count = 0  # количество хороших оценок
    for i in range(7):  # проходим по первым 7 оценкам - заполняем начальные значения bad_count good_count
        if seq[i] == 2 or seq[i] == 3:
            bad_count += 1
        elif seq[i] == 5:
            good_count += 1
    if bad_count == 0 and good_count > answer:  # если нет плохих оценок и ответ лучше - изменяем ответ
        answer = good_count
    for i in range(7, m):  # проходим окном 7 по оценкам
        # обновляем bad_count good_count при правой границе окна
        if seq[i] == 2 or seq[i] == 3:
            bad_count += 1
        elif seq[i] == 5:
            good_count += 1
        # обновляем bad_count good_count при левой границе окна
        if seq[i - 7] == 2 or seq[i - 7] == 3:
            bad_count -= 1
        elif seq[i - 7] == 5:
            good_count -= 1
        if bad_count == 0 and good_count > answer:  # если нет плохих оценок и ответ лучше - изменяем ответ
            answer = good_count
    # ответ
    print(answer)