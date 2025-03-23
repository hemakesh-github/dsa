def crafting(a, b, s):
    toChangeFlag = False
    toChangeVal = 0
    m = float('inf')
    
    for i in range(s):
        if a[i] < b[i]:
            if toChangeFlag:
                return "NO"
            toChangeVal = b[i] - a[i]
            toChangeFlag = True
        else:
            m = min(a[i] - b[i], m) 
    if toChangeVal <= m:
        return "YES"
    return "NO"


n = int(input())
ans = []
for i in range(n):
    s = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans.append(crafting(a, b, s))
for i in ans:
    print(i)
    