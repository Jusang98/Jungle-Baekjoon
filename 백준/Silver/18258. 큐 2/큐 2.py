import sys

N = int(sys.stdin.readline())
queue = []
cnt = 0
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) - cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
            cnt += 1
    elif command[0] == "size":
        print(len(queue) - cnt)
    elif command[0] == "empty":
        if len(queue) - cnt == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(queue) - cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
    elif command[0] == "back":
        if len(queue) - cnt == 0:
            print(-1)
        else:
            print(queue[-1])
