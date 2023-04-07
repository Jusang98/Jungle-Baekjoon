import sys

a = sys.stdin.readline().split()
x = int(a[0])
y = int(a[1])
w = int(a[2])
h = int(a[3])

min1 = w - x
min2 = h - y

print(min(x, y, min1, min2))
