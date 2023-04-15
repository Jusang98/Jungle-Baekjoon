import sys

N = int(sys.stdin.readline())
Liquid = list(map(int, sys.stdin.readline().split()))
Liquid.sort()
start = 0
end = len(Liquid) - 1
mix = sys.maxsize  # 최솟값 변수 초기화

while start < end:
    newmix = Liquid[start] + Liquid[end]
    if abs(newmix) < mix:  # 기존의 mix값보다 new mix의 절대값이 작을떄
        mix = abs(newmix)
        ans = [Liquid[start], Liquid[end]]
    if newmix < 0:  # 0보다 작으면 s +
        start += 1
    elif newmix > 0:  # 0보다 크면 e -
        end -= 1
    else:
        break

ans.sort()
print(ans[0], ans[1])
