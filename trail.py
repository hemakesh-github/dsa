def trail(m,n, matrix, path):
    i , j = 0, 0
    for p in path:
        if p == 'D':
            x = 0
            for k in range(n):
                x -= matrix[i][k]
            matrix[i][j] = x
            i += 1
        else:
            x = 0
            for k in range(m):
                x -= matrix[k][j]
            matrix[i][j] = x
            j += 1
    x = 0
    if m < n:
        for k in range(m):
            x -= matrix[k][j]
        matrix[i][j] = x
    else:
        for k in range(n):
            x -= matrix[i][k]
        matrix[i][j] = x
    return matrix

t = int(input())
ans = []
for i in range(t):
    m, n = map(int, input().split())
    path = input()
    matrix = []
    for i in range(m):
        matrix.append(list(map(int, input().split())))
    ans.append(trail(m, n, matrix, path))

for m in ans:
    for i in range(len(m)):
        print(m[i][0], end ="")
        for j in range(1,len(m[0])):
            print(f" {m[i][j]}", end = "")
        print()