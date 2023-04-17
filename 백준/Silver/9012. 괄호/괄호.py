import sys

T = int(sys.stdin.readline())
vps = []

for _ in range(T):
    cnt = 0
    n = sys.stdin.readline().strip()
    vps = list(n)
    for i in vps:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")
