import sys


def binary(arr, start, end):
    result = 0
    while start <= end:
        middle = (start + end) // 2
        total = 0
        for tree in arr:
            if tree > middle:
                total += tree - middle
        if total < M:
            end = middle - 1
        else:
            result = middle
            start = middle + 1
    return result


N, M = map(int, sys.stdin.readline().split())
treeList = list(map(int, sys.stdin.readline().split()))
a = binary(treeList, 0, max(treeList))
print(a)
