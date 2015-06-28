"""
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]


for x in all_perms("1234"):
    print x

"""

tryout = list("1234")


def permute(a,k,n):
    if k == n:
        print a
    else:
        for i in xrange(k,n):
            a[k],a[i] = a[i],a[k]
            permute(a,k+1,n)
            a[i],a[k] = a[k],a[i]

permute(tryout,0,len(tryout))
