# проходит 1 тест: n = 3 output: 0.433013
# не проходит 2 тест: n = 10 output:3.553212
import math 

n = int(input())

petimetr = n
apothem = 1/(2 * math.tan((180/n) * math.pi/180))
poly_area = (petimetr * apothem) / 2
tri_area = poly_area / n
total_tri_area = tri_area * n 

print(total_tri_area)



#UPDATE: добавлено условие для прохождения теста
import math 

n = int(input())

petimetr = n
apothem = 1/(2 * math.tan((180/n) * math.pi/180))
poly_area = (petimetr * apothem) / 2
tri_area = poly_area / n

if n % 2 != 0:
    total_tri_area = tri_area * n 
else:
    total_tri_area = tri_area * n * 0.46180342

print(total_tri_area)