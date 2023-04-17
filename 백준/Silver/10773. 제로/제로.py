import sys

K = int(sys.stdin.readline())
n = []
for _ in range(K):
    a = int(sys.stdin.readline())
    if a != 0:
        n.append(a)
    else:
        n.pop(-1)
print(sum(n))