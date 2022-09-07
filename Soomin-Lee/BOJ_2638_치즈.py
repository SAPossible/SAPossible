from collections import deque
import sys

input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def check():
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    queue = deque([(0, 0)])
    cnt = 0

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and not board[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

                if board[nr][nc]:
                    visited[nr][nc] += 1

                    if visited[nr][nc] >= 2:
                        board[nr][nc] = 0
                        cnt += 1

    return cnt

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ret = 0

while True:
    if check():
        ret += 1
    else:
        break

print(ret)