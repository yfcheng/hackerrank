words = ['senthil','yahoo','yelp','deepa','manya','google','mcafee','microsoft']
import random
parse = []
for x in xrange(100):
    parse.append(random.choice(words))


#Method 1: sort based on items

from collections import defaultdict
catalog = defaultdict(int)

for x in parse:
    catalog[x]+=1

print sorted(catalog.iteritems(),key = lambda x: x[1],reverse=True)[:3]

#Method 2: use priority queue

"""
    class Top3Max:
        constructor initialize dictionary
        push element ->
            add
            heapify
        pop element ->
            add
            heapify
"""


