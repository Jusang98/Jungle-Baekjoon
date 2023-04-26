# 첫째줄에 N개의 도시
# 둘째줄에 다른 도시로 가는 버스의 개수 M
# 셋쨰줄부터 출발 도시 A, 도착 도시 B, 버스 비용 P 정보 입력
# 마지막 줄에 출발 도시 S, 도착 도시 E 입력
# 출발 도시에서 도착 도시로 가는 비용 최소화 최소 비용 출력
# 다익스트라 문제 - 우선순위 큐 사용 - 알아서 최단거리 노드 가장 앞으로 정렬해준다
import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())  # 도시 개수
M = int(sys.stdin.readline())  # 버스 개수
tree = [[] for _ in range(N + 1)]  # 그래프
distance = [int(1e9) for _ in range(N + 1)]  # 사이거리 무한대로 초기화
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())  # 버스의 출발도시, 도착도시, 비용 정보
    tree[A].append([B, C])
S, E = map(int, sys.stdin.readline().split())  # 출발도시, 도착도시


def bfs(start):
    heap = []
    distance[start] = 0
    heappush(heap, [distance[start], start])
    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:  # 기존의 비용이 새로운 비용보다 적으면 무시
            continue
        for x in tree[now]:
            cost = dist + x[1]  # 비용 + 인접도시 버스 비용
            if cost < distance[x[0]]:  # 기존의 비용보다 새로들어온 비용이 싸면
                heappush(heap, [cost, x[0]])  # 업데이트
                distance[x[0]] = cost  # 업데이트


bfs(S)
print(distance[E])
