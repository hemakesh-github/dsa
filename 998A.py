def fib(arr):
    d = {}
    d[arr[0] + arr[1]] = 1
    if arr[2] - arr[1] in d:
        d[arr[2] - arr[1]] += 1
    else:
        d[arr[2] - arr[1]] = 1
    if arr[3] - arr[2] in d:
        d[arr[3] - arr[2]] += 1
    else:
        d[arr[3] - arr[2]] = 1
    
    return max(d.values())


n = int(input())
ans = []
for i in range(n):
    arr = list(map(int, input().split()))
    ans.append(fib(arr))
for i in ans:
    print(i)