inpu = [int(x) for x in raw_input().split(" ")]
N, K = inpu[0], inpu[1]
boys = [int(x) for x in raw_input().split(" ")]
girls = [int(x) for x in raw_input().split(" ")]
boys = sorted(boys)

print N,K
print boys
print girls