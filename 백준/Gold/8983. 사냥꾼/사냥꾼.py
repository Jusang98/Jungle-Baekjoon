import sys

# 첫줄 입력 M은 사대의 수 N은 동물의 수 L은 사정거리
M, N, L = map(int, sys.stdin.readline().split())
# 두 번쨰 줄 입력은 사대의 좌표 입력
saro = list(map(int, sys.stdin.readline().split()))
# 그 이후 줄들은 동물의 좌표
animal = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
saro.sort()
count = 0
for a, b in animal:
    if b > L:  # 동물 좌표 b가 L보다 크면 잡을수없다.
        continue
    start = 0
    end = len(saro) - 1
    # 동물을 잡을수있는 최소값, 최대값
    Min = a + b - L
    Max = a - b + L
    while start <= end:
        mid = (start + end) // 2
        if Min <= saro[mid] <= Max: # 동물을 잡을수있을떄 count+=1
            count += 1
            break
        elif saro[mid] < Max: # 동물을 못잡고 Max보다 작을떄
            start = mid + 1
        else:
            end = mid - 1
print(count)

