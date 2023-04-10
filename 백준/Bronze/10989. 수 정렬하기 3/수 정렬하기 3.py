import sys

# 받는 갯수
N = int(sys.stdin.readline())
# 리스트 10000 제한
arr = [0] * 10001
# N 만큼 받아
for _ in range(N):
    num = int(sys.stdin.readline())
    # arr[num]에 num이 들어온 갯수 카운팅
    arr[num] += 1

for i in range(10001):
    # arr[i]가 0이 아니면
    if arr[i] != 0:
        # arr[num]에 num 갯수만큼 출력!
        for j in range(arr[i]):
            print(i)


