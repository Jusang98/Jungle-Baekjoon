import sys
import math

condition = list(map(int, sys.stdin.readline().split()))

A = condition[0]  # 달팽이가 낮에 올라갈 높이 ex) input(2)
B = condition[1]  # 달팽이가 밤에 내려올 높이 ex) input(1)
V = condition[2]  # V높이의 나뭇가지 ex) input(5)
days = (V - B) / (A - B) # 정상에 올라가면 달팽이는 내려오지않는다.
# ex) V/(A-B)를 할시 5/1 5일이 걸린다고 출력되지만 실제론 4일이 걸린다. 따라서 V에서 B를 미리 뺴줌으로서
print(math.ceil(days))  # math.ceil로 나머지가 남으면 올림 즉 아직 달팽이가 갈 길이가 남아있다면 day 올림