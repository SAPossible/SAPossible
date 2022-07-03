import sys
from collections import deque


def set_outside(row, col):
    outside = deque([(row, col)])
    visited[row][col] = 2

    while outside:
        r, c = outside.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not CHEESE[nr][nc]:
                visited[nr][nc] = 2
                outside.append((nr, nc))


def check_status(row, col):
    checked = 0

    for d in range(4):
        if visited[row+dy[d]][col+dx[d]] == 2:
            checked += 1
    if checked >= 2:
        melted.append((row, col))


# input
N, M = map(int, sys.stdin.readline().split())
CHEESE = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# init
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
result = 0

while True:
    visited = [[0] * M for _ in range(N)]
    melted = []

    set_outside(0, 0)  # 외부 설정

    for r in range(N):
        for c in range(M):
            if CHEESE[r][c]:
                check_status(r, c)  # 상태 확인: 외부와의 접촉면이 2개 이상인지

    if melted:  # 녹여!
        for r, c in melted:
            CHEESE[r][c] = 0
        result += 1
    else:
        break

print(result)

"""
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0 
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0
"""
