import sys
l, k = [], int(sys.stdin.readline())
for i in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        l.append(num)
    else:
        l.pop()
if len(l) == 0:
    print(0)
else:
    print(sum(l))