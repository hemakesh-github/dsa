def d(n, a):
    for i in range(n-1):
        if a[i] > a[i+1]:
            return 'NO'
        x = min(a[i], a[i+1])
        a[i] -= x
        a[i+1] -= x
    return "YES"
t = int(input())
ans = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans.append(d(n, a))
for i in ans:
    print(i)