# 동적 프로그래밍
import sys

n = int(sys.stdin.readline())  # n번째 피보나치

nazzi = [0, 1]  # 리스트

for i in range(2, n + 1):  # 리스트에 피보나치 수를 계산하여 저장
    nazzi.append(nazzi[i - 1] + nazzi[i - 2])

print(nazzi[n]) # n번째 피보나치