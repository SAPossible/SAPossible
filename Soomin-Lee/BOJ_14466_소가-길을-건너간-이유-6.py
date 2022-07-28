from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 < nr <= N and 0 < nc <= N and not visited[nr][nc]:
                if (nr, nc) not in roads[r][c]:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1


N, K, R = map(int, input().split())
roads = [[[] for _ in range(N+1)] for _ in range(N+1)]

for i in range(R):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    roads[r1][c1].append((r2, c2))
    roads[r2][c2].append((r1, c1))

cows = [tuple(map(int, input().split())) for _ in range(K)]
cnt = 0

for k in range(K):
    visited = [[0] * (N+1) for _ in range(N+1)]
    bfs(cows[k][0], cows[k][1])

    for s in range(k+1, K):
        if not visited[cows[s][0]][cows[s][1]]:
            cnt += 1

print(cnt)