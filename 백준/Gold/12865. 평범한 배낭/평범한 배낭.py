# import sys
#
# # 첫줄에 물건의 개수 N , 버틸수있는 무게 K
# # 두번째 줄부터 물건 무게 W, 가치 V 입력받기
import sys

n, k = map(int, sys.stdin.readline().split()) # 물건의 개수 n, 버틸수있는 무게 k
arr = [] # 물건 무게 가치 받아놓을 배열만들어놓기
for _ in range(n): # 물건의 개수만큼
    w, v = map(int, sys.stdin.readline().split()) # 무게, 가치
    arr.append([w, v])

d = [0 for _ in range(k + 1)]  # 무게 리스트

for item in arr: # arr에 담겨있는 item 하나씩 꺼내온다
    w, v = item
    # print(w, v)
    for i in range(k, w - 1, - 1): # 최대 무게부터 역순으로 물건 무게 체크
        d[i] = max(d[i], d[i - w] + v) # 현재 물건이랑 가치 합과 최대값 비교

print(d[-1])







