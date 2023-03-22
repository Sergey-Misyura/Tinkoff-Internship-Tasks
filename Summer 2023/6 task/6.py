n, s = map(int, input().split())
scores = []

for _ in range(n):
    scores.append(tuple(map(int, input().split())))

left, right = 1, 10 ** 9 + 1

def reach(mid):
    count, sum_scores = 0, 0
    arr_scores = []
    for score in scores:
        if mid <= score[0]:
            sum_scores += score[0]
            count += 1
        elif score[1] < mid:
            sum_scores += score[0]
        else:
            arr_scores.append(score[0])

    min_count = max(0, int((len(scores) + 1) // 2) - count)
    if min_count <= len(arr_scores):
        i = 0
        while i != len(arr_scores) - min_count:
            sum_scores += arr_scores[i]
            i += 1
        while i != len(arr_scores):
            sum_scores += mid
            i += 1
    else:
        return False
        
    return sum_scores <= s

scores.sort()
while right > left + 1:
    middle = (right + left) // 2
    if reach(middle):
        left = middle
    else:
        right = middle


print(left)