import sys

a = int(sys.stdin.readline())

for _ in range(a):
    b = list(sys.stdin.readline().rstrip())
    result = 0
    score = 1
    for i in b:
        if i == "O":
            result += score
            score += 1
        else:
            score = 1
    print(result)
