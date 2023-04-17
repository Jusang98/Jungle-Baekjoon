import sys

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

AxB = [[0] * K for _ in range(N)]
for row in range(N):
    for column in range(K):
        for i in range(M):
            AxB[row][column] += A[row][i] * B[i][column]
for j in AxB:
    for num in j:
        print(num, end=" ")
    print()
