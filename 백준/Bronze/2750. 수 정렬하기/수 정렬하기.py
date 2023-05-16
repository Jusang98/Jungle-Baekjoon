import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
nums.sort()
for j in nums:
    print(j)