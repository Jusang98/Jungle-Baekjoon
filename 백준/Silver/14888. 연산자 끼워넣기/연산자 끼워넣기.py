# 첫쨰 줄엔 수의 개수 N 과 N-1개수의 연산자 M 입력
# 둘째 줄엔 수열 A 입력
# 셋째줄엔 합이 N-1 인 4개의 정수가 주어지는데 각 + - * / 의 개수가 입력된다.
# N개의 수와 N-1의 연산자가 주어졌을떄 만들수있는 식의 최대값과 최소값을 출력하면 된다.
# 주의할 점 - 연산자 우선순위를 무시하며 나눗셈은 몫만 취한다(/ 대신 // 사용하기), 음수를 나눌경우 양수로 바꿔 나누고 몫을 음수로 다시 바꾸는 형식으로
# 수열의 길이가 6이고 연산자의 개수가 5개인 경우엔 총 60가지를 만들수있다. N*(N-1) x2인가? ? (N이 2일떄 제외하고)

import sys

N = int(sys.stdin.readline())  # 수의 개수
A = list(map(int, sys.stdin.readline().split()))  # 수열
add, sub, mul, div = map(int, sys.stdin.readline().split())  # 연산자 개수

max_value = -10 ** 9
min_value = 10 ** 9


def dfs(v, arr):
    global add, sub, mul, div, max_value, min_value
    if v == N:  # 수열 다받았을때 최대값 최소값
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if add > 0:
            add -= 1
            dfs(v + 1, arr + A[v])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(v + 1, arr - A[v])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(v + 1, arr * A[v])
            mul += 1
        if div > 0:
            div -= 1
            dfs(v + 1, int(arr / A[v]))
            div += 1


dfs(1, A[0])

print(max_value)
print(min_value)
