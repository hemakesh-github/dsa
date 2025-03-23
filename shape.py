def per(n, m, op):
    ans = m * n*4
    for i in range(1, n):
        x, y = max((m - op[i][0]), 0), max((m -op[i][1]), 0)
        # print(x, y)
        ans -= 2 * (x + y)
    return ans

t = int(input())
ans = []
for k in range(t):
    n, m = map(int, input().split())
    op = []
    for i in range(n):
        op.append(list(map(int, input().split())))
    ans.append(per(n, m, op))
    
for i in ans:
    print(i)
    
