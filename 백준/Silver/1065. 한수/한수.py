import sys

N = int(sys.stdin.readline())
cnt = 0
for i in range(1, N + 1):  
    if i < 100:
        cnt += 1
    else:
        a = list(str(i))  
        if int(a[1]) - int(a[0]) == int(a[2]) - int(a[1]):  
            cnt += 1
print(cnt)