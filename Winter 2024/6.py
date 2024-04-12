class LazySegmentTree:
    def __init__(self, data):
        self.data = data
        self.tree = [0] * (4 * len(self.data))
        self.lazy = [0] * (4 * len(self.data))
        self._init(1, 0, len(self.data) - 1)

    def _init(self, i, tl, tr):
        if tl == tr:
            self.tree[i] = self.data[tl]
            return self.tree[i]
        self.tree[i] = max(self._init(i * 2, tl, (tl + tr) // 2),
                           self._init(i * 2 + 1, (tl + tr) // 2 + 1, tr))
        return self.tree[i]

    def update(self, left, right, add):
        self._update(1, left, right, add, 0, len(self.data) - 1)

    def _update(self, i, ql, qr, val, tl, tr):
        if qr < tl or tr < ql:
            return
        if ql <= tl and tr <= qr:
            self.lazy[i] += val
            self.tree[i] += val
            return
        self.lazy[i * 2] += self.lazy[i]
        self.lazy[i * 2 + 1] += self.lazy[i]
        self.tree[i] += (self.lazy[i] + val)
        self.lazy[i] = 0
        self._update(i * 2, ql, qr, val, tl, (tl + tr) // 2)
        self._update(i * 2 + 1, ql, qr, val, (tl + tr) // 2 + 1, tr)

    def query(self, left, right, k, b):
        return self._query(1, left, right, 0, len(self.data) - 1, k, b)

    def _query(self, i, ql, qr, tl, tr, k, b):
        if qr < tl or tr < ql:
            return 0
        if tl == ql and tr == qr:
            if ql == qr:
                return min(self.tree[i], k * (tl + 1) + b)
            tmid = (tl + tr) // 2
            tmid_val = k * (tmid + 1) + b

            self.lazy[i * 2] += self.lazy[i]
            self.lazy[i * 2 + 1] += self.lazy[i]
            self.tree[i * 2] += self.lazy[i]
            self.tree[i * 2 + 1] += self.lazy[i]
            self.lazy[i] = 0

            if self.tree[i * 2 + 1] >= tmid_val:
                return self._query(i * 2 + 1, max(ql, tmid + 1), qr, tmid + 1, tr, k, b)
            else:
                return max(self._query(i * 2, ql, min(qr, tmid), tl, tmid, k, b), self.tree[i * 2 + 1])

        tmid = (tl + tr) // 2
        self.lazy[i * 2] += self.lazy[i]
        self.lazy[i * 2 + 1] += self.lazy[i]
        self.tree[i * 2] += self.lazy[i]
        self.tree[i * 2 + 1] += self.lazy[i]
        self.lazy[i] = 0
        return max(
            self._query(i * 2, ql, min(qr, tmid), tl, tmid, k, b),
            self._query(i * 2 + 1, max(ql, tmid + 1), qr, tmid + 1, tr, k, b)
        )

if __name__ == "__main__":
    # считываем данные
    n, q = map(int, input().split())  # числа в массиве, число запросов
    a = list(map(int, input().split()))  # массив чисел
    tree = LazySegmentTree(a)  # создаем из массива чисел дерево отрезков

    for _ in range(q):  # выполняем запросы
        query = input().strip()
        if query[0] == '+':  # если запрос добавить - выполняем tree.update
            l, r, x = map(int, query[2:].split())
            tree.update(l-1, r-1, x)

        elif query[0] == '?':  # если запрос получить - выполняем печатаем tree.query
            l, r, k, b = map(int, query[2:].split())
            print(tree.query(l-1, r-1, k, b))
