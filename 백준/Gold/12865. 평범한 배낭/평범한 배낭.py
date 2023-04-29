import sys

# 첫줄에 물건의 개수 N , 버틸수있는 무게 K
# 두번째 줄부터 물건 무게 W, 가치 V 입력받기
N, K = map(int, sys.stdin.readline().split())
item = [[0, 0]]
bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    item.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = item[i][0]
        value = item[i][1]

        if j < weight: # 현재 물건이 해당열 무게보다 크다면 담을수없는 물건임으로 [이전물건][현재무게]
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(value + bag[i - 1][j - weight], bag[i - 1][j])

print(bag[N][K])
