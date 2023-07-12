import sys
while True:
    n, a, w = sys.stdin.readline().split();
    if n == "#":
        break
    if int(a) > 17 or int(w) >= 80:
        print(n, "Senior")
    else:
        print(n, "Junior")

