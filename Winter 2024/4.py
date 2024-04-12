# считываем данные
n, k = map(int, input().split())  # размер дерева и количество интересных для Боба компаний.

graph = [[] for _ in range(n)]  # граф
nodes_val = [0] * n  # значение узла - цена компании, ее номер
companies = dict()  # словарь компаний название - номер
node_price = ['inf'] * n  # цену поддерева и компании в поддереве

cur_n = 1  # номер текущей компании
companies[input().strip()] = cur_n  # добавляем компанию в словарь companies

for _ in range(k-1):  # добавляем остальные компании в словарь companies
    cur_n = cur_n << 1
    companies[input().strip()] = cur_n

root = 0  # корневой элемент
for i in range(n):  # добавляем вершины в граф
    p, a, c = input().strip().split()  # p - номер родителя вершины или 0, если вершина является корнем, a - стоимость пакета акций, с - название компании
    p, a = int(p), int(a)
    if p > 0:  # если не корень - добавляем компанию в список к родителю
        graph[p-1].append(i)
    else:  # если корень - меняем значение корневого элемента
        root = i
    nodes_val[i] = (a, companies[c])  # добавляем цену компании и ее номер в nodes_val

def dfs(node):  # функция обхода в глубину
    if not graph[node]:  # если лист, цена и компании поддерева равны цене в узле и компании в узле
        node_price[node] = nodes_val[node]
        return nodes_val[node]

    price, comps = nodes_val[node]  # цена компании, ее номер
    for next_node in graph[node]:  # проходим dfs по соседям
        res = dfs(next_node)  # общая цена, компании поддерева
        price += res[0]  # увеличиваем цену текущего поддерева на цену поддерева соседа
        comps |= res[1]  # добавляем к компаниям comps компании из res

    node_price[node] = price, comps  # записываем цену поддерева и компании в узле поддереве node
    return price, comps  # возвращаем цену поддерева и компании в узле поддереве node

# обходим дерево от root
dfs(root)

prices = [price for price, comps in node_price if comps == (1 << k) - 1]  # список цен с количеством нужных компаний
# ответ
if not prices:  # если список пустой - ответ -1
    print(-1)
else:  # если есть общая цена, берем минимум
    print(min(prices))