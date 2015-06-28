
a = [2,6,4,2,3]
g = []
sum = 0
g.append(a[0])
for x in xrange(1,len(a)-1):
    sum += a[x]
    g.append(sum / x+1)
g.append(len(a)-1)

print g
