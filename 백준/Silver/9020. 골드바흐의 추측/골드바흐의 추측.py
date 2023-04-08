import sys


def prime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


t = int(sys.stdin.readline())
n = []
for _ in range(t):
    n.append(int(sys.stdin.readline().strip()))
for j in range(len(n)):
    q, w = n[j] // 2, n[j] // 2
    while True:
        if prime(q) and prime(w):
            print(q, w)
            break
        else:
            q -= 1
            w += 1
