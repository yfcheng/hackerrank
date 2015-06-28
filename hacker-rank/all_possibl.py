def begin_end(st):
    first = st[0]
    last = st[len(st) - 1]
    return 1 if first == last else 0

N = int(raw_input())
s = raw_input()
sum = 0

for c in xrange(N):
    for i in xrange(1,N-c+1):
        sum += begin_end(s[c:c+i])
        #print s[c:c+i]
print sum
