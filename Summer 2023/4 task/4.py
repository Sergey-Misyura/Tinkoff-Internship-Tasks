from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))


max_count = 0
counts_num= defaultdict(int)
repeats_count = defaultdict(int)
prefix_max_len = 0

for i in range(len(a)):

    counts_num[a[i]] +=1
    repeats_count[counts_num[a[i]]]+=1
    if counts_num[a[i]]!=1:
        repeats_count[counts_num[a[i]]-1]-=1
        
    if counts_num[a[i]] == i or counts_num[a[i]] == i+1:
        max_count = counts_num[a[i]]
    elif counts_num[a[i]] == max_count + 1 and repeats_count[counts_num[a[i]]] > 1:
        max_count = counts_num[a[i]]
    
       
    if (repeats_count[max_count+1]==1 and max_count * repeats_count[max_count] == i-max_count) or (repeats_count[1]==1 and max_count * repeats_count[max_count] == i) or (max_count==1 and repeats_count[1]==i+1) or (max_count * repeats_count[max_count] == i+1):
        prefix_max_len = i+1

        
print(prefix_max_len)