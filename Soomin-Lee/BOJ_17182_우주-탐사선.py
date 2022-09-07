import sys
input = sys.stdin.readline

def find_Route(start, next, time, cnt):
    global total

    if cnt == N-1:
        total = min(total, time)
        return

    if time > total:
        return

    for n in range(N):
        if not visit[n]:
            visit[n] = 1
            find_Route(next, n, time + graph[next][n], cnt + 1)
            visit[n] = 0


N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

visit = [0] * N
visit[K] = 1

total = 1e7

for i in range(N):
    if not visit[i]:
        visit[i] = 1
        find_Route(K, i, graph[K][i], 1)
        visit[i] = 0

print(total)
