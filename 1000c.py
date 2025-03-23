def removeTwo(n, mat):
    
    
    for _ in range(2):
        k = getToRemove(mat)
        for i in range(n):
            mat[k][i] = 0 
            mat[i][k] = 0
    
    
def getToRemove(mat, n):
    maxS = 0
    k = -1
    for i in range(n):
        s = 0
        for j in range(n):
            s += mat[i][j]
        if s > maxS:
            k = i 
            maxS = s
    return k
t = int(input())
for i in range(t):
    n = int(input())
    d = {}
    
    for i in range(n):
        i, j = map(int, input().split())
        mat[i-1][j-1] = 1
        mat[j-1][i-1] = 1
    removeTwo(n, mat)