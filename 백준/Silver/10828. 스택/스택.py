import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            a = stack.pop(-1)
            print(a)
    elif command[0] == "size":
        b = len(stack)
        print(b)
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
