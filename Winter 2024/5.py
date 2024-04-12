# считываем данные
n, m, q = map(int, input().split())  # дети, пары, события
border = int(n ** 0.5)  # граница

nodes_value = [0] + list(map(int, input().split()))  # значения в узлах
degree = [0] * (n + 1)  # количество соседей

edges = [[] for _ in range(n + 1)]  # соединения
light_edges = [[] for _ in range(n + 1)]  # легкие грани
heavy_edges = [[] for _ in range(n + 1)]  # тяжелые грани
heavy_add_value = [0] * (n + 1)  # добавляемые значения на тяжелых гранях

for _ in range(m):  # проходим по парам добавляем в список соединений и количество соседей
    v, u = map(int, input().split())
    edges[v].append(u)
    edges[u].append(v)
    degree[v] += 1
    degree[u] += 1

for from_ in range(1, n + 1):  # определяем тяжелые и легкие вершины
    for to_ in edges[from_]:
        if degree[to_] > border:
            heavy_edges[from_].append(to_)
        else:
            light_edges[from_].append(to_)

for _ in range(q):  # проходим по событиям
    query = input().strip()
    if query[0] == '?':   # если событие посчитать
        v = int(query[2:])  # вершина
        ans = nodes_value[v]  # ответ
        for u in heavy_edges[v]:  # собираем значения из тяжелых узлов
            ans += heavy_add_value[u]
        # ответ
        print(ans)

    elif query[0] == '+':  # если событие отправить стикеры
        v, x = map(int, query[2:].split())  # вершина отправитель, количество стикеров

        if degree[v] > border:  # если вершина тяжелая - оставляем количество стикеров в ней
            heavy_add_value[v] += x
        else:  # иначе рассылаем соседям
            for u in heavy_edges[v]:
                nodes_value[u] += x
            for u in light_edges[v]:
                nodes_value[u] += x
