import sys

n = int(sys.stdin.readline())


# n: 원판 갯수 , 1번기둥(start) - s기둥, 2번 기둥(middle) - m 기둥, 3번 기둥(end) - e 기둥
def hanoi(n, s, e):
    m = 6 - s - e  # 2번기둥
    if n == 1:
        print(s, e) #
    else:
        hanoi(n - 1, s, m) # n-1 의 원판을 전부 s -> m (그 안에서 print 1,3 -> 1,2 ->  3,2...)
        print(s, e) #남은 하나를 s -> e 1,3
        hanoi(n - 1, m, e) # m에 위치한 n-1의 원판을 전부 -> e로


print(2 ** n - 1) # n개의 판 이동횟수 구하는 식
if n <= 20: # 조건
    hanoi(n, 1, 3)
