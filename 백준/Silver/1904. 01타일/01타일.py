import sys
n = int(sys.stdin.readline())

nazzi = [0] * (n + 1) # 리스트 n +1 만큼 만들어두고 ==> nazzi[0] = 0 부터 시작
nazzi[1] = 1 # 1일땐 1 타일 1개
if n > 1:
    nazzi[2] = 2 # 2일땐 1, 00 2개
# 3일땐 100, 001, 111 3개
# 4일땐 0011, 0000, 1001, 1100, 1111 5개 즉 피보나치 수열을 이룬다.
# print(nazzi)
for i in range(3, n+1):
    nazzi[i] = (nazzi[i - 1] + nazzi[i - 2]) % 15746 # 메모리초과 - 출력이 크기 떄문에 나눠준다 근데 왜 15746?
#     # 파이썬 정수형은 메모리 고정이 아니다.
# #
# #
print(nazzi[n])