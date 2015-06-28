
phone = {   '0' : ['0'],
            '1' : ['1'],
            '2' : ['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
         }

def get_keycodes(ph,num):
    if len(num) == 0:
        return []
    keycodes = ph[num[0]]
    i = 1
    for e in xrange(1,len(num)):
        tempkeyCodes = []
        for newChar in ph[num[e]]:
            for old in keycodes:
                tempkeyCodes.append(old+newChar)
        keycodes = tempkeyCodes
    return sorted(keycodes)

if __name__ == '__main__':
    print get_keycodes(phone,'')
    print get_keycodes(phone,'26')
    print get_keycodes(phone,'1800')
    print get_keycodes(phone,'123')

