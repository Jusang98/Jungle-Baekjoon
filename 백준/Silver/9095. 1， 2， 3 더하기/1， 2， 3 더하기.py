import sys


def sums(n):  # 1 - 1, 2 - 2, 3 - 4 , 4 - 7, 5 - 13 , 6 - 24
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sums(n - 1) + sums(n - 2) + sums(n - 3)


T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    print(sums(N))
