# limitation - 제한 사항 함수 > 퀸이 같은 행에 있으면 안됨, 퀸이 대각선에 있으면 안됨
# 입력 N은 NxN 체스판 row[0]*n 으로 사용
# result - > =+ 로 출력할 방법갯수 카운팅
# 출력 퀸을 놓을수있는 방법 출력
import sys

n = int(sys.stdin.readline())
row = [0] * n
cnt = 0


def limitation(a):
    for i in range(a):
        if row[a] == row[i] or abs(row[a] - row[i]) == abs(a - i):
            return False
    return True


def queen(a):
    global cnt
    if a == n:
        cnt += 1
        return
    else:
        for i in range(n):
            row[a] = i
            if limitation(a):
                queen(a + 1)


queen(0)
print(cnt)
