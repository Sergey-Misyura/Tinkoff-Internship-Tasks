# считываем данные
n, dir = input().split()  # сторона матрицы, направление поворота
n = int(n)
mtr = []  # матрица
for _ in range(n):
    mtr.append(input().split())

answer = []  # массив координат ячеек для перестановки
if dir == 'R':  # для правого поворота
    rg_ls = n - 2  # индекс последнего переставляемого элемента в текущей строке
    for row in range(n // 2):  # проходим по строкам до средней, так как далее поворот уже не нужен, числа будут уже переставлены
        for col in range(row, rg_ls + 1):  # проходим по столбцам до последнего индекса rg_ls, сужая квадрат перестановки слева, так как там уже нужные числа
            # достаточно 3х перестановок для 4х чисел расположенных по сторонам квадрата, меняемых как при повороте матрицы на 90
            # по кругу направо меняем значения в ячейках
            mtr[col][rg_ls + 1], mtr[n - row - 1][n - col - 1], mtr[n - col - 1][row], mtr[row][col] = mtr[row][col], mtr[col][rg_ls + 1], mtr[n - row - 1][n - col - 1], mtr[n - col - 1][row]
            # записываем 3 перестановки в ответ (отличается от обмена выше из-за функций питона)
            answer.append(' '.join([str(x) for x in (col, rg_ls + 1, row, col)]))
            answer.append(' '.join([str(x) for x in (row, col, n - col - 1, row)]))
            answer.append(' '.join([str(x) for x in (n - col - 1, row, n - row - 1, n - col - 1)]))
        rg_ls -= 1  # уменьшаем крайний правый индекс элемента в текущей строке
else:  # для левого поворота, как для правого, но в другую сторону
    rg_ls = n - 2
    for row in range(n // 2):
        for col in range(row, rg_ls + 1):
            # по кругу налево меняем значения в ячейках
            mtr[n - col - 1][row], mtr[n - row - 1][n - col - 1], mtr[col][rg_ls + 1], mtr[row][col] = mtr[row][col], mtr[n - col - 1][row], mtr[n - row - 1][n - col - 1], mtr[col][rg_ls + 1]
            answer.append(' '.join([str(x) for x in (n - col - 1, row, row, col)]))
            answer.append(' '.join([str(x) for x in (row, col, col, rg_ls + 1)]))
            answer.append(' '.join([str(x) for x in (col, rg_ls + 1, n - row - 1, n - col - 1)]))
        rg_ls -= 1
if not answer:  # если ответ пуст - ответ 0
    print(0)
else:  # иначе выводим количество перестановок, и сами перестановки
    print(len(answer))
    print(*answer, sep='\n')