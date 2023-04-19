import sys

# 탑의 수
N = int(sys.stdin.readline())
# 탑의 높이
tops =  [0] + list(map(int, sys.stdin.readline().split()))

result = [0] * (N + 1)

stack = []

for i in range(1, N + 1):
    # Stack에 탑의 정보가 남아있다면
    while stack:
        # 탑의 높이가 Stack TOP의 높이보다 크다면
        if tops[i] > stack[-1][0]:
            # Stack TOP 제거
            stack.pop()
        # 탑의 높이가 Stack TOP의 높이보다 작다면
        else:
            # 현재 탐색하고 있는 탑의 레이저를 수신 받을 수 있는 탑의 위치를 저장
            result[i] = stack[-1][1]
            break

    # 탑을 Stack에 삽입
    stack.append((tops[i], i))

# 결과 출력
for i in range(1, N + 1):
    print(result[i], end=" ")
