import sys

n = int(sys.stdin.readline())

nums = map(int, sys.stdin.readline().split())
count = 0


# i 3일떄 계산
def prime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


for j in nums:
    if prime(j):
        count += 1
print(count)
