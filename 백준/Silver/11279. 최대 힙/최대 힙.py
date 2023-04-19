import heapq
import sys

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))
    else:
        heapq.heappush(heap, x * -1)
