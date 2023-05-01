import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())  # 지원자 수
    apply = [0] * (n + 1)  # 미리 0부터 n+1까지 배열 만들어놓기
    for _ in range(n):
        a, b = map(int, input().split())
        apply[a] = b  # 정렬을 안해줘도 1부터 오름차순으로 배열에 들어가게 된다.

    count = 1  # 1차 서류 면접 점수 1등은 무조건 합격
    highest = apply[1]  # 1차 서류 면접 점수 1등 합격자의 2차 면접 점수을 최고 점수로 지정
    for i in range(2, n + 1):  # 2등부터 1등의 2차 면접 점수와 비교한다
        if apply[i] < highest:  # 2차 면접점수가 1등합격자의 2차 면접 점수보다 더 높으면 합격시키고 최고 점수로 갱신해준다.
            highest = apply[i]
            count += 1
    print(count)
