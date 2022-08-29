import sys
from collections import deque


def check_cond(row, col, nrow, ncol):
    return True if L <= abs(F[row][col] - F[nrow][ncol]) <= R else False


def find_alliances(row, col):
    q = deque([(row, col)])  # BFS 수행을 위한 deque
    alliances = [(row, col)]  # 반환 리스트
    visited[row][col] = True

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + DY[d], c + DX[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and check_cond(r, c, nr, nc):
                visited[nr][nc] = True
                q.append((nr, nc))
                alliances.append((nr, nc))
    return alliances


def move(alliances):
    population = sum([F[row][col] for row, col in alliances]) // len(alliances)  # 이동 후 인구수 계산
    for row, col in alliances:
        F[row][col] = population  # 계산된 인구수 반영


N, L, R = map(int, sys.stdin.readline().split())
F = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # INPUT

DY = [-1, 0, 1, 0]
DX = [0, 1, 0, -1]  # 4방위 탐색을 위한 리스트
flag = True  # 무한 반복을 방지하기 위한 플래그 변수
ans = 0  # OUTPUT 변수

while flag:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                alliances = find_alliances(r, c)  # 연합 국가를 찾기 위한 BFS 수행 함수
                if len(alliances) > 1:  # 연합 국가를 찾으면 반환 리스트에 최소 2개의 요소 존재
                    move(alliances)  # 인구 이동 수행 함수
                    flag = True  # 인구 이동이 발생했으므로 동일 절차 반복
    if flag:  # 인구 이동이 발생했으므로
        ans += 1

print(ans)  # OUTPUT
