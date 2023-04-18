import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque()
newQ = []
for i in range(N):
    queue.append(i + 1)
while len(queue) >= 1:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    newQ.append(queue.popleft())

print("<", end="")
for i in range(len(newQ)):
    if i == len(newQ) - 1:
        print(newQ[i], end=">")
    else:
        print(newQ[i], end=", ")
