# 

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr = [name, score]
        records.append(arr)
    records.sort(key = lambda x : x[1])
    u_score =  sorted(set(s[1] for s in records))
    second_lowest = u_score[1]
    
    res = []
    for i,j in records:
        if j == second_lowest:
            res.append(i)
    res.sort()
    for i in res:
        print(i)            
        