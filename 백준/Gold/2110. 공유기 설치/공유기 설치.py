import sys

N, C = map(int, sys.stdin.readline().split())
home = []
for _ in range(N):
    home.append(int(sys.stdin.readline()))

home.sort()
start = 0
end = home[-1]
ans = 0


def binary(arr, s, e):
    while s <= e:
        m = (s + e) // 2
        current = arr[0]
        count = 1
        for i in range(len(arr)):
            if arr[i] >= current + m:
                count += 1
                current = arr[i]
        if count >= C:
            global ans
            ans = m
            s = m + 1
        else:
            e = m - 1


binary(home, start, end)
print(ans)
