d = {
    "++X": 1,
    "X++": 1,
    "--X": -1,
    "X--": -1
}

n = int(input())
x = 0
for i in range(n):
    s = input()
    x += d[s]
print(x)