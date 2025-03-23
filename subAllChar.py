i = 0
j = 0
map = {}
s = "aabcbcdbba"
n = len(s)
ans = n

ansStr = s
for i in s:
    map[i] = 0
i = 0
sets = set()
while(j < n):
    if s[j] in map:
        sets.add(s[j])
        map[s[j]] += 1
    while len(sets) == len(map.keys()):
        if ans > j-i+1:
           ansStr = s[i: j+1]
           ans = j-i+1 
        map[s[i]] -= 1
        if map[s[i]] == 0:
            sets.remove(s[i])
        i+=1
    j+=1
print(ansStr)

