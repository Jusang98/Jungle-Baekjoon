import sys

n = int(sys.stdin.readline())

nums = map(int, sys.stdin.readline().split())
count = 0

for i in nums:
    if i > 1:
        noCount = 0
        for j in range(2, i):

            if i % j == 0:
                noCount += 1
        if noCount == 0:
            count += 1
print(count)
