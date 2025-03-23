def daba(s):
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = [i]
        else:
            d[s[i]].append(i)
    ans = 0
    for i in d:
        for j in range(len(d[i])-1):
            for k in range(j+1, len(d[i])):
                ans += d[i][k] - d[i][j] -1
            
    return ans

print(daba(input("")))
    
