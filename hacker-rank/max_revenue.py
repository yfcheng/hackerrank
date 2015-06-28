n,m = raw_input().split()
rev_contrs = [int(x) for x in raw_input().split()]
rev_contrs.sort(reverse = True)

print n,m
print rev_contrs

int_cont = 0
limit = 0
next = 1
num = 0
while (rev_contrs(limit) - rev_contrs(next)) < m:
	limit += 1
	next += 1
print rev_contrs(limit)