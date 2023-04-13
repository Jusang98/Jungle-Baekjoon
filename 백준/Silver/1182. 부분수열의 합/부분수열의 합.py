import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
cnt = 0
a = []


def sol(s):
    global cnt
    if sum(a) == S and len(a) > 0:  # 종료 조건
        cnt += 1
    for i in range(s, N):
        a.append(nums[i])
        sol(i + 1)
        a.remove(nums[i])


sol(0)
print(cnt)
