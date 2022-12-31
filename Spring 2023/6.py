n = int(input())

max_XOR=0
arr=[]

for i in range(n):
    num = int(input())
    if num not in arr:
        val = 0
        arr.append(num)
        for i in range(0, len(arr)-1):
            val = arr[i] ^ arr[i + 1]
            max_XOR = max(max_XOR, val)
    print(max_XOR)