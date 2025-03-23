t = int(input())
ans = []
for i in range(t):
    a, b = map(int, input().split())
    if a == 1 and b == 1:
        ans.append(1)
    else:
        ans.append(b - a)
for i in ans:
    print(i)