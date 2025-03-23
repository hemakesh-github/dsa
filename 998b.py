def john(n, m, mat):
    for i in range(n):
        mat[i].sort()
    
    order = []
    min_e = 0
    
    for i in range(n):
        min_val = float('inf')
        for j in range(n):
            if mat[j][0] < min_val :
                if len(order) > 0 and mat[j][0] > mat[order[-1]-1][0]:
                    min_e = j
                    min_val = mat[j][0]
                elif len(order)== 0:
                    min_e = j
                    min_val = mat[j][0]
        order.append(min_e + 1)
    for i in range(1, m):
        if mat[order[n-1]-1][i-1] < mat[order[0]-1][i]:
            pass
        else:
            return [-1]
        for j in range(1, n):
            if mat[order[j-1]-1][i] < mat[order[j]-1][i]:
                continue
            else:
                return [-1]
    return order

t = int(input())
ans = []
for i in range(t):
    mat = []
    n, m = map(int, input().split())
    for j in range(n):
        mat.append(list(map(int, input().split())))
    ans.append(john(n, m, mat))
for i in ans:
    
    print(*i)
        
    