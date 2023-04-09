import sys

n = int(sys.stdin.readline())


def factorial(a):
    if a > 0:
        return a * factorial(a - 1)
    else:
        return 1


print(factorial(n))
