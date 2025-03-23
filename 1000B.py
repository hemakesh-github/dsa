def subseq(n, l, r, arr):
    a1 = sorted(arr[:r])
    a2 = sorted(arr[l-1:n+1])
    ans1 = 0
    ans2 = 0
    for i in range(r-l+1):
        
        ans1 += a1[i]
        ans2 += a2[i]
    return min(ans1, ans2)




t = int(input())
ans = []
for i in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    ans.append(subseq(n, l, r, arr))
for i in ans:
    print(i)
    
# def minSubSum(arr, low, high, s, n):
#     if n <= 0:
#         return s
    
        
#     if low <= high:
#         x = minSubSum(arr, low+1, high, s+arr[low], n-1)
#         y = minSubSum(arr, low + 1, high, s, n)
#         return min(x, y)
#     else:
#         return float('inf')

