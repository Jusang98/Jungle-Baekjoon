import sys

# 테스트케이스 T, 동전가짓수 N 동전 , 금액 오름차순으로 입력 coin ,금액 M, 만드는 가짓수 출력

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0] * (M + 1)
    dp[0] = 1  # 동전을 안쓰는 가짓수 1 추가
    for i in coin:  # 동전 리스트
        for j in range(1, M + 1):  # M+1 까지 리스트
            if j >= i:  # j가 해당동전보다 크면
                dp[j] += dp[j - i]  # DP[j - i] 의 가짓수를 dp[j]에 더해주면서 M까지 반복
    print(dp[M])
