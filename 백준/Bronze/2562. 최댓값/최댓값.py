import sys

numbers = [int(sys.stdin.readline()) for _ in range(9)]
print(max(numbers))
print(numbers.index(max(numbers)) + 1)
