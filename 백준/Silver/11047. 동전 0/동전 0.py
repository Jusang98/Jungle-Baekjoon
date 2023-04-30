import sys

# 첫줄 가지고 있는 동전 종류 n개 만들고자하는 k
# 둘쨰 줄 부터 동전의 가치 오름차순으로 나타남
# coin(i)는 coin(i-1)의 배수라는 조건이 중요하다
# 따라서 코인중 가장 큰놈부터 나눈만큼 카운팅하며 나머지를 k에 저장 반복
n, k = map(int, sys.stdin.readline().split())
coin = list(int(sys.stdin.readline()) for _ in range(n))
count = 0
for i in reversed(range(n)):
    count += k // coin[i]  # 카운트 값에 k를 coin으로 나눈값을 더해줌
    k = k % coin[i]
print(count)
