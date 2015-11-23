input = [1, 2, 6, 5, 9]

# array of the products of all integers
# except the integer at each index:
# [540, 270, 90, 108, 60] # [2*6*5*9, 1*6*5*9, 1*2*5*9, 1*2*6*9, 1*2*6*5]

prod_indxes_before = []
before, after = 1, 1

for x in xrange(len(input)):
	prod_indxes_after.insert(0, after)
	after *= input[len(input) - x - 1]

out = []
for x in xrange(len(input)):
	val = prod_indxes_after[x] * before
	out.append(val)
	before *= input[x]
print out