N = int(input())
a = list(map(int, input().split()))

hash_d = {0: -1}
pref_sum = 0
segments = []
len_a = len(a)

for i in range(len_a):

	pref_sum += a[i]

	if pref_sum in hash_d:
		segments.append((hash_d.get(pref_sum) + 1, i))

	hash_d[pref_sum] = i

total_segments = 0
if segments!= []:
    total_segments = (segments[0][0]+1)*(len_a-segments[0][1])

if len(segments)>1:
    for seg_idx in range(1, len(segments)):
        total_segments += (segments[seg_idx][0]-segments[seg_idx-1][0])*(len_a - segments[seg_idx][1])

print(total_segments)