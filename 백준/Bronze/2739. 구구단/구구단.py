import sys

a = int(sys.stdin.readline())

for i in range(1, 10):
    result = a * i

    print(a, '*', int(i), "=", result)
