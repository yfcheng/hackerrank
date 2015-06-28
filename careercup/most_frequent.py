from collections import defaultdict

words = ['Jellicle', 'Cats', 'are', 'black', 'and', 'white,', 'Jellicle', 'Cats', 'are', 'rather', 'small;', 'Jellicle', 'Cats', 'are', 'merry', 'and', 'bright,', 'And', 'pleasant', 'to', 'hear', 'when', 'they', 'caterwaul.', 'Jellicle', 'Cats', 'have', 'cheerful', 'faces,', 'Jellicle', 'Cats', 'have', 'bright', 'black', 'eyes;', 'They', 'like', 'to', 'practise', 'their', 'airs', 'and', 'graces', 'And', 'wait', 'for', 'the', 'Jellicle', 'Moon', 'to', 'rise.', '']

c = defaultdict(int)
for x in words:
    c[x]+=1

print sorted(c.items(),key = lambda x:x[1],reverse=True)[:3]


words = ['cat', 'star', 'act', 'god', 'arts', 'dog', 'rats']
print sorted(words,key=lambda x:sorted(x))
