# https://www.hackerrank.com/contests/pythonist3/challenges/compress-the-string

S = str(input())
cnt = 0
out = []
prev = ""
for e in S:
    if e != prev and len(prev) > 0:
        out.append((cnt, int(prev)))
        cnt = 0
    prev = e
    cnt += 1
out.append((cnt, int(prev)))
a = ""
for item in out:
    print(item, end=' ')