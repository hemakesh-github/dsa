
def pal(t):
    ans = [1, 1]
    for i in range(2, t-2):
        ans.append(i)
    ans.append(1)
    ans.append(2)
    return ans

n = int(input())
ans = []
for i in range(n):
    t = int(input())
    ans.append(pal(t))
for i in ans:
    print(*i)
