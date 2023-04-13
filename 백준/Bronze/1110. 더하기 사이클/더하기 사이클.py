import sys

N = int(sys.stdin.readline())
number = N
cnt = 0
while True:
    a = number // 10  # 10의 자리수
    b = number % 10  # 1의 자리수
    c = (a + b) % 10  # 자리합의 1의 자리수
    number = (b * 10) + c  # 기존 num의 1의 자리수 + 자리합의 1의 자리수
    cnt += 1
    if number == N:  # 종료 조건
        break
print(cnt)
