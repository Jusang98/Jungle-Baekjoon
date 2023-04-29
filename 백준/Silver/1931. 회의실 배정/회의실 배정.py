import sys

# N개의 회의
# meeting
# 각 회의의 시작 시간 start, 끝난 시간 end 같을수있다
# 겹치지않게 회의 최대 개수 찾아보자

N = int(sys.stdin.readline()) # 회의 개수
meetings = [] # 회의 리스트
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append([start, end])

meetings = sorted(meetings, key=lambda x: x[0])
meetings = sorted(meetings, key=lambda x: x[1])

lastmeeting = 0  # 전 회의의 종료 시간
conut = 0  # 회의 개수

for i, j in meetings:
    if i >= lastmeeting:  # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
        conut += 1
        lastmeeting = j

print(conut)
