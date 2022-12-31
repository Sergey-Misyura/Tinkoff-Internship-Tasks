import math

n = int(input())

nod = 1
if n % 2 == 0:
    print(int(n/2), int(n/2))
else:
    nod_current = 3
    nod_max = round(math.sqrt(n)+1)
    while (nod == 1) and (nod_current != nod_max):
        nod = nod_current if n % nod_current == 0 else nod
        nod_current +=1
        
    if nod != 1:
        print(nod, int((n/nod - 1) * nod))
    else:
        print(1, n-1)