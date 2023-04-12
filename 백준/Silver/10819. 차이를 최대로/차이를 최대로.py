import sys
import itertools

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

per = itertools.permutations(A)

res = 0
for i in per:
    s = 0
    for j in range(1, N):
        s += abs(i[j - 1] - i[j])
    if res < s:
        res = s
print(res)
