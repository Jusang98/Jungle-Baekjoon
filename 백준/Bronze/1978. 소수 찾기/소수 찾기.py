import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
count = 0


def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for j in numbers:
    if prime(j):
        count +=1


print(count)