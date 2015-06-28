"""
https://www.hackerrank.com/challenges/candies
20		10
2		2
4		4
2		2
6		6
1		1
7		7
8		8
9		9
3		2
2		1
1		
3		
4		18
5		
6		
7		
4		
3		
2		
1		
"""

def sum_to_n_terms(n):
    return n * (n + 1) / 2

N = int(raw_input())
scores = []

for x in xrange(N):
    scores.append(int(raw_input()))
out = 0
p_score,c_score = 0,0
p_candy,c_candy = 0,0
for score in scores:
    if score > p_score:

