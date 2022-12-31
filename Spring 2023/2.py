import math

a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

mean_value_sum = int((x/a + y/b + z/c))

result = math.factorial(mean_value_sum+2) / (math.factorial(2)*math.factorial(mean_value_sum))
print(int(result))