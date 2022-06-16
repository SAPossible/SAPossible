import sys
from collections import deque


def check_default_cond(row, col, visited):
    return True if 0 <= row < R and 0 <= col < C and not visited[row][col] else False


def check_border():
    # 1. 좌측 상단 모서리에서 BFS 수행 및 치즈 경계선 파악
    q = deque([(0, 0)])
    visited = [[False] * C for _ in range(R)]
    visited[0][0] = True

    while q:
        row, col = q.popleft()

        for d in range(4):
            nrow, ncol = row + dy[d], col + dx[d]
            if check_default_cond(nrow, ncol, visited):
                visited[nrow][ncol] = True

                # 1.1. 경계선 처리
                if BOARD[nrow][ncol] == 1:
                    BOARD[nrow][ncol] = 0
                else:
                    q.append((nrow, ncol))


def count():
    return sum(map(sum, BOARD))


R, C = map(int, sys.stdin.readline().split())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
result = [(0, count())]  # 2. 매 회차의 결과를 저장하는 리스트

while result[-1][1]:
    check_border()
    result.append((result[-1][0] + 1, count()))

# 3. 문제에서 요구하는 값만 인덱싱
print(result[-1][0])
print(result[-2][1])
