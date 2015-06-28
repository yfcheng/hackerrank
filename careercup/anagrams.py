words = ['tsar','star','tac','act','stra','tca']

print "Method 1"
print sorted(words,key = lambda x:sorted(x))

from collections import defaultdict

print "\nMethod 2"
d = defaultdict(list)

for x in words:
    temp_w = "".join(sorted(x))
    d[temp_w] += [x]

output = []
for x in d.keys():
    output += d[x]

print output

print "\n Method 3"

def merge_data(left,right):
    result = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        left_var = sorted(left[left_idx].lower())
        right_var = sorted(right[right_idx].lower())
        if left_var <= right_var:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result


def merge_sort(m):
    if len(m) <= 1:
        return m
    middle = len(m) / 2
    left = m[:middle]
    right = m[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge_data(left,right))

print merge_sort(words)


