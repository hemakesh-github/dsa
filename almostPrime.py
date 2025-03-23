def sieve(n):
    primes= [[]for i in range(n+1)]
    for i in range(2, n):
        if len(primes[i]) == 0:
            for j in range(2*i, n+1, i):
                    primes[j].append(i)
    return primes

def getAlmostPrimes(n):
    primes = sieve(n)
    c = 0
    # print(primes)
    for i in range(n+1):
        if len(primes[i]) == 2:
            c+=1
        # print(i, primes[i])
    return c

print(getAlmostPrimes(int(input())))