def dfs(row, col, type, steps, visited):  # поиск в глубину от текущей клетки
    if grid[row][col] == 'F':  # когда попали на финиш - возвращаем число шагов
        return steps

    visited.add((row, col))  # добавляем текущую клетку к посещенным
    # проверяем изменился ли тип фигуры
    if grid[row][col] == 'K':  # для коня
        type = 'K'
    elif grid[row][col] == 'G':  # для короля
        type = 'G'

    res = float('inf')  # мин число шагов от текущей клетки до финиша
    # рекурсивно запускаем dfs по направлениям от текущей клетки
    if type == 'K':  # для коня
        for shf in shf_k:  # проходим по сдвигам для коня
            # если новая клетка в пределах grid и она еще не была посещена
            if row + shf[0] < n and row + shf[0] > -1 and col + shf[1] < n and col + shf[1] > -1 and (row + shf[0], col + shf[1]) not in visited:
                res = min(res, dfs(row + shf[0], col + shf[1], type, steps + 1, visited.copy()))  # обновляем res, запуская dfs c сделанным шагом в новую клетку
    else:  # для короля аналогично
        for shf in shf_g:
            if row + shf[0] < n and row + shf[0] > -1 and col + shf[1] < n and col + shf[1] > -1 and (row + shf[0], col + shf[1]) not in visited:
                res = min(res, dfs(row + shf[0], col + shf[1], type, steps + 1, visited.copy()))
    # возвращаем res
    return res

# считываем данные
n = int(input().strip())  # размер доски
grid = []  # доска
start, finish = (0, 0), (0, 0)  # координаты старта и финиша
for i in range(n):
    row = list(input().strip())
    for j in range(n):
        if row[j] == 'S':
            start = (i, j)
        elif row[j] == 'F':
            finish = (i, j)
    grid.append(row)

shf_k = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]  # сдвиги для коня
shf_g = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # сдвиги для короля
visited = set()  # множество посещенных клеток
answer = dfs(start[0], start[1], 'K', 0, visited)  # ответ, запускаем dfs из start с конем, анчальный шаг 0
if answer == float('inf'):  # если не дошли до финиша - ответ -1
    print(-1)
else:  # иначе, ответ
    print(answer)