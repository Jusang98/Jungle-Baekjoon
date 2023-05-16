import sys

N = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())
findlist = list(map(int, sys.stdin.readline().split()))

numlist.sort()


def binarysearch(num):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if num == numlist[mid]:
            return True
        elif num < numlist[mid]:
            right = mid - 1
        elif num > numlist[mid]:
            left = mid + 1

for i in findlist:
    if binarysearch(i):
        print(1)
    else:
        print(0)