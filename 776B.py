def sieve(n):
    primes= [1]*(n+2)
    for i in range(2, int((n+2)**0.5)+1):
        if primes[i] == 1:
            for j in range(2*i, n+2, i):
                primes[j] = 2
    return primes[2:]

n = int(input())
a = sieve(n)
if n <= 2:
    print(1)
else:
    print(2)

print(*a, sep=' ')



