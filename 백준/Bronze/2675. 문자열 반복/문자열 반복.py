import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    b = list(sys.stdin.readline().strip().split(" "))
    c = int(str(b[0]))
    d = list(str(b[1]))
    f = ""
    for i in range(len(d)):
        e = str(d[i])*c
        f += e
    print(f)

