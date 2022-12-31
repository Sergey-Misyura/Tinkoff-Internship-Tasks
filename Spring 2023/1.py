n = int(input())
s = [i for i in input().split()]
b = input()

ugly_words = 0
patterns = ['YY', 'BB']
mask_cursor = 0
for word in s:

    if (patterns[0] in b[mask_cursor: mask_cursor+len(word)]) or (patterns[1] in b[mask_cursor: mask_cursor+len(word)]):
        ugly_words += 1 
    
    mask_cursor = len(word)
    
print(ugly_words)