# считываем данные
n, m = map(int, input().split())  # строки, столбцы матрицы
matrix = []  # матрица
for i in range(n):
    row = input().split()
    matrix.append(row)

matrix = list(zip(*matrix[::-1]))  # поворачиваем матрицу на 90 вправо
# ответ
print(*[' '.join(row) for row in matrix], sep='\n')