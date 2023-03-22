peoples = list(map(int, input().split()))

answer = 'NO'
if peoples[0]<=peoples[1]<=peoples[2]<=peoples[3]:
    answer = 'YES'
elif peoples[0]>=peoples[1]>=peoples[2]>=peoples[3]:
    answer = 'YES'
    
print(answer)