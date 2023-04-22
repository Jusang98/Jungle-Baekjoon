# 이진트리를 전위탐색할시에 부모 노드값은 배열 [0] 이고 부모노드값보다 커지는 숫자가 나올때까지 왼쪽 서브트리 그 이후엔 오른쪽 서브 트리다.
# 전위 탐색은 부모노드 -> 왼쪽 자식 -> 오른쪽 자식 후위 탐색은 왼쪽 -> 오른쪽 -> 부모노드 순이다.
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

pre = []
while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break


def prepost(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break
    prepost(start + 1, mid - 1)  # 왼쪽 트리
    prepost(mid, end)  # 오른쪽 트리
    print(pre[start])  # 루트 노드


prepost(0, len(pre) - 1)
