n, m, k = tuple(map(int, input().split()))

if (n*k) % m != 0:
    time = (n*k) // m +1
else:
    time = (n*k) // m
print(time)