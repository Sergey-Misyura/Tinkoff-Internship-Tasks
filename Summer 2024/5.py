from functools import cache
import sys

sys.setrecursionlimit(100000)

@cache
def dfs(row, col):  # поиск в глубину, ищет макс возможное для получения число грибочков
    if row >= n or col > 2 or col < 0 or grid[row][col] == 'W':  # если вышли за границы или наткнулись на кусты - возвращаем 0
        return 0
    total = 0  # число получаемых грибов с текущей клетки
    for i in range(3, 0, -1):  # запускаем dfs для 3х возможных шагов
        total = max(total, dfs(row + 1, col + 2 - i))  # обновляем total
    if grid[row][col] == 'C':  # если в нашей клетке гриб - увеличиваем total
        total += 1
    # возвращаем число получаемых грибов с текущей клетки
    return total

# считываем данные
n = int(input().strip())  # количество строк в лесу
grid = []  # сетка леса
for _ in range(n):
    grid.append(list(input().strip()))
answer = 0  # ответ
for i in range(3):  # выбираем максимальный из dfs для клеток в 0 строке
    answer = max(answer, dfs(0, i))
# ответ
print(answer)