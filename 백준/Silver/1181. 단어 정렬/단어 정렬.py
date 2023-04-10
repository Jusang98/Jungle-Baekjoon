import sys

n = int(sys.stdin.readline())
words = []
for i in range(n):
    a = sys.stdin.readline().strip()
    words.append(a)

b = list(set(words))

b.sort()
for _ in range(len(b)):
    c = min(b, key=len)
    print(c)
    b.remove(c)