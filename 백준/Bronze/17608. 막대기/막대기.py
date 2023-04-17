import sys

N = int(sys.stdin.readline())
sticks = []
a = []
cnt = 1
for _ in range(N):
    sticks.append(int(sys.stdin.readline().strip()))
a.append(sticks.pop())
for _ in range(len(sticks)):
    b = []
    b = sticks.pop()
    if a[0] < b:
        cnt += 1
        a[0] = b
print(cnt)
