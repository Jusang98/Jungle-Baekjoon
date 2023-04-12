import sys


def z(n, r, c, res):
    length = 2 ** n  # 배열 길이
    half = length // 2  # 사분면으로 만들기위한 배열길이의 절반길이 구하기
    if n == 1: # 재귀 종료조건 2x2 4 최소 사분면이 만들어질 경우
        print(2 * r + c + res)  # row가 늘어나면 도착횟수가 2씩 늘어나고 colunm이 늘어나면 1씩 늘어난다.
        return

    if r >= half and c >= half:  # 4사분면일떄 조건
        z(n - 1, r - half, c - half, res + 3 * half * half)
    elif r >= half > c:  # 3사분면일때 조건
        z(n - 1, r - half, c, res + 2 * half * half)
    elif r < half <= c:  # 2사분면일때 조건
        z(n - 1, r, c - half, res + half * half)
    else:  # 1사분면일때 조건
        z(n - 1, r, c, res)


n, r, c = map(int, sys.stdin.readline().split())

z(n, r, c, 0)
