def twoFrogs(a, b):
    if (abs(a-b) - 1) %2:
        return 'YES'
    return 'NO'

n = int(input())
ans = []
for i in range(n):
    (n, a, b) = map(int, input().split())
    ans.append(twoFrogs(a, b))

for i in ans:
    print(i)