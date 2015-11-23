#https://www.hackerrank.com/contests/zenhacks/challenges/pairing

N = int(input())
bags = {}
for i in range(N):
    _in = input()
    sh = _in.split(' ')
    tup = (str(sh[0]), sh[1], str(sh[2]))
    if tup not in bags:
        bags[tup]= []
    pairs = bags[tup]
    pairs.append(sh[3])
    bags[tup] = pairs

arrange = 0

for v in bags.values():
    p = {}
    for e in v:
        cnt = 0
        if e in p:
            cnt = p[e]
        p[e] = cnt + 1
    if 'L' not in p:
        p['L'] = 0
    if 'R' not in p:
        p['R'] = 0
    arrange += min(p['L'], p['R'])

print(arrange)

