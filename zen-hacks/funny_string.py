def diff_ascii(first, second):
    return abs(ord(first) - ord(second))

def funny_or_not_funny(inp):
    rev = inp[::-1]
    #print rev
    i = 1
    while (i < len(inp)):
        if diff_ascii(inp[i],inp[i-1]) != diff_ascii(rev[i], rev[i-1]):
            return "Not Funny"
        i = i + 1
    return "Funny"
    
if __name__ == "__main__":
    N = int(raw_input())
    for instr in xrange(N):
        print funny_or_not_funny(raw_input())
