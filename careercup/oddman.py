a = ["cat","star","act","god","arts","dog","rats"]
c = sorted(a,key=lambda x:sorted(x))
print c

def get_oddman_out(c):
    d = {}
    for e in c:
        if d.has_key(e):
            d[e] += 1
        else:
            d[e] = 1
    
    first = d[d.keys()[0]]
    second = d[d.keys()[1]]
    third = d[d.keys()[2]]
    if first == second and second != third:
        return d.keys()[2]
    if first != second and second == third:
        return d.keys()[0]
    if first == third and second != third:
        return d.keys[1]
    
    for eac in d.items():
        if eac[1] != first:
            return eac[0]
    return d.keys[0]

numbers = [1,2,4,2,3,1,4,3,5,5,6,6,7,7,7,7]

print get_oddman_out(numbers)
