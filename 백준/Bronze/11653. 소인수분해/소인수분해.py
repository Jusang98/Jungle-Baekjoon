import sys

N = int(sys.stdin.readline())
a = 2
result = 0

while a <= N:
    if N == 1:
        break
    elif N % a == 0:
        print(a)
        N /= a
    else:
        a += 1



