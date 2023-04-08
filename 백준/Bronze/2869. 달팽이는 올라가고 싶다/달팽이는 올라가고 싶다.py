import sys
import math

condition = list(map(int, sys.stdin.readline().split()))
a = condition[0]
b = condition[1]
v = condition[2]
d = (v - a) / (a - b)
print(math.ceil(d) + 1)
