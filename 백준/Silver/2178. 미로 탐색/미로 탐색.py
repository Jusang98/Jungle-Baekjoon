import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = []

# 미로 받기
for i in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

# 갈수있는 상하좌우
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    while queue:
        row1, col1 = queue.popleft()
        for drow, dcol in d:
            if 0 <= row1 + drow < N and 0 <= col1 + dcol < M: # 미로 벽 밖으로 나가면 안되게 조건문 걸기
                if maze[row1 + drow][col1 + dcol] == 1:
                    maze[row1 + drow][col1 + dcol] = maze[row1][col1] + 1
                    queue.append((row1 + drow, col1 + dcol))


bfs(0, 0)
print(maze[N - 1][M - 1])
