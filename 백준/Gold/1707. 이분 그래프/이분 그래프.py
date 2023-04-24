import sys

sys.setrecursionlimit(10 ** 6)
K = int(sys.stdin.readline())


def dfs(v, color):
    visit[v] = color  # 방문한 v에 색 할당
    for i in tree[v]:
        if visit[i] == 0:  # 안가본곳이면 방문
            if not dfs(i, -color):
                return False
        elif visit[i] == visit[v]:  # 방문한 곳인데 색이 동일하면 이분그래프가 아니다!
            return False
    return True


for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(V + 1)]  # 그래프
    visit = [0] * (V + 1)  # 방문 체크용
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)  # 무방향 그래프
        tree[b].append(a)

        bipartite = True  # 이분그래프인지 확인

    for i in range(1, V + 1):
        if visit[i] == 0:  # 방문한 지점이 아니라면 dfs 실행
            bipartite = dfs(i, 1)
            if not bipartite:
                break
    print("YES" if bipartite else "NO")
