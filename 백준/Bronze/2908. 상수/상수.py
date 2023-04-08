import sys

nums = list(map(int, sys.stdin.readline().split()))
reversNums = []
for i in range(len(nums)):
    revers = int(str(nums[i])[::-1])
    reversNums.append(revers)

print(max(reversNums))
