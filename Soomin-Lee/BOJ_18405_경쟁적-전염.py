from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs():
    while queue:
        v, r, c, t = queue.popleft()

        if t == S:
            return

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 0:
                    board[nr][nc] = v
                    queue.append((v, nr, nc, t + 1))


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

queue = deque([])

for r in range(N):
    for c in range(N):
        if board[r][c] != 0:
            queue.append((board[r][c], r, c, 0))

queue = deque(sorted(queue, key=lambda x: x[0]))

bfs()

print(board[X-1][Y-1])