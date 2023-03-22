N = int(input())
s = input()

min_len = -1
if N >= 4:
    sym_dict = {}
    sym_list = []
    idx_el = 0
    while len(sym_dict)!=4 and idx_el < len(s):
        sym_dict[s[idx_el]] = idx_el
        idx_el+=1

    if len(sym_dict)==4:
        for elem in sym_dict:
            sym_list.append([elem, sym_dict[elem]])
        
        sym_list.sort(key=lambda x: x[1])
        min_len = sym_list[3][1]-sym_list[0][1]+1
        
        for idx_s in range(idx_el, len(s)):
            for idx_list in range(0,4):
                if s[idx_s]==sym_list[idx_list][0]:
                    if idx_list==0:
                        sym_list.pop(0)
                        sym_list.append([s[idx_s], idx_s])
                        min_len = min(min_len, sym_list[3][1]-sym_list[0][1]+1)
                    elif idx_list==3:
                        sym_list[idx_list][1]=idx_s
                    elif idx_list==2:
                        sym_list[idx_list], sym_list[idx_list+1] = sym_list[idx_list+1], [s[idx_s],idx_s]
                    else:
                        sym_list[idx_list], sym_list[idx_list+1], sym_list[idx_list+2] = sym_list[idx_list+1], sym_list[idx_list+2], [s[idx_s],idx_s]
                        

print(min_len)
