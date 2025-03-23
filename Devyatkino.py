def Devyatkino(n):
    t = n%10
    if t == 7:
        return 0
    n = n//10
    i = 1
    ans = float('inf')
    # print(n)
    nines = 9
    while(n>0):
        d = n%10
        t = t + (n%10) * (10**i)
        n = n//10
        if d == 7:
            return 0
        elif d < 7:
            a = 7 * (10**i) - t 
            if a%nines != 0:
                if (nines * (a//nines + 1)) - a <= nines:
                    ans = min(ans, a//nines + 1) 
            else:
                if (nines * (a//nines)) - a <= nines:
                    ans = min(ans, a//nines) 
        nines += 9 * (10**i)
        i += 1
    a = 7 * (10**(i)) - t 
    if a%nines != 0:
        if (nines * (a//nines + 1)) - a <= nines:
            ans = min(ans, a//nines + 1) 
    else:
        if (nines * (a//nines)) - a <= nines:
                    ans = min(ans, a//nines ) 
    return ans


t = int(input())
ans = []
for i in range(t):
    n = int(input())
    ans.append(Devyatkino(n))
for i in ans:
    print(i)