def game(n, arr, key):
    d = [0] * key
    for i in range(n):
        if arr[i] >= key:
            continue
        d[arr[i]] += 1
    ans = 0
    for k in range(1,(key//2) + 1):
        req = abs(key - k)
        if req == k:
            ans += d[k]//2
            d[k] -= d[k]//2
            continue
        if d[req]>0: 
            x = min(d[req], d[k])
            d[req] -= x
            d[k] -= x
            ans += x
    return ans 

t = int(input())
ans = []
for i in range(t):
    n, key = map(int, input().split())
    arr = list(map(int, input().split()))
    ans.append(game(n, arr, key))
for i in ans:
    print(i)
            