import sys

# n: 원판 갯수 , s기둥, m 기둥, e 기둥
n = int(sys.stdin.readline())


def hanoi(n, s, e):
    m = 6 - s - e
    if n == 1:
        print(s, e)
        return
    else:
        hanoi(n - 1, s, m)
        print(s, e)
        hanoi(n - 1, m, e)


print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3)
