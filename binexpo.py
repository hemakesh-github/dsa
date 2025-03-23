def binExpo(a, b):
    ans = 1
    while(b > 0):
        if b &1:
            ans = (ans * a)%10
        a = (a*a)%10
        b = b>>1
    return ans%10

t = int(input())
ans = []
for i in range(t):
    a, b = map(int, input().split())
    ans.append(binExpo(a, b))

for i in ans:
    print(i)


