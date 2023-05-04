# n 밖으로 나가면 안되고
# 갔다가 만약 가장 오른쪽 아래에 도달했다면 멈추고 count 업?
import sys

n = int(sys.stdin.readline())
jump = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1  # 초기값

# print(dp)
count = 0
# 반복문을 돌며 모두 탐색
for row in range(n):  # 아래는 row 오른쪽은 column
    for column in range(n):
        moveNumber = jump[row][column]  # 해당 발판 숫자
        if row == n - 1 and column == n - 1:  # 가장 오른쪽 아래에 도달했을때 저장된 dp 출력
            print(dp[row][column])
            break
        # 발판 숫자 만큼 오른쪽으로 갈떄 게임판에서 벗어나지않는 경우 체크
        if column + moveNumber < n:
            dp[row][column + moveNumber] += dp[row][column]
        # 발판 숫자 만큼 아래로 갈때 게임판에서 벗어나지않는 경우 체크
        if row + moveNumber < n:
            dp[row + moveNumber][column] += dp[row][column]


