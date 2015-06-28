def begin_end(st):
    first = st[0]
    last = st[len(st) - 1]
    return 1 if first == last else 0

N = int(raw_input())
s = raw_input()
sum = begin_end(s)
for i in xrange(1,N):
    st = 0
    end = st + i
    while end <= N:
        sum += begin_end(s[st:end])
        print s[st:end]
        st += 1
        end += 1


print sum
