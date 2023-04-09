import sys

# paper 는 종이 가로 세로 입력
# width는 가로 height는 세로
# t는 테스트 케이스 수
# a는 0일땐 가로 1일땐 세로 자르기
paper = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())
width = [0, paper[0]]
height = [0, paper[1]]
for _ in range(t):
    c = list(map(int, sys.stdin.readline().split()))
    if c[0] == 0:
        height.append(c[1])
    else:
        width.append(c[1])
width.sort()
height.sort()
widthList = []
heightList = []
for i in range(len(width)-1):
    widthList.append(width[i+1] - width[i])

for j in range(len(height)-1):
    heightList.append(height[j+1] - height[j])

print(max(widthList)*max(heightList))

