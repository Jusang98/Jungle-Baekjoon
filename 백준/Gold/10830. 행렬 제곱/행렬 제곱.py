import sys

n, b = map(int, sys.stdin.readline().split())
A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))


def mul(n,a,b):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result


def cal(n,b,A):
    if b == 1:
        return A
    elif b == 2:
        return mul(n,A,A)
    else:
        temp = cal(n, b // 2, A)
        if b % 2 == 0:
            return mul(n,temp,temp)
        else:
            return mul(n,mul(n,temp,temp),A)

result = cal(n,b,A)

for row in result:
    for num in row:
        print(num % 1000,end= ' ')
    print()