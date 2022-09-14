from collections import deque

N, M = map(int, input().split())
mat = [input() for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visit[0][0][0] = 1
# visit[r][c][0] : 벽을 안 부수고 해당 좌표까지 왔을 때 거리
# visit[r][c][1] : 벽을 부수고 해당 좌표까지 왔을 때 거리


def function(sr, sc):
    # is_break : 벽을 부쉈는지 여부
    # 0: 아직 부순 적 없음, 1: 부순 적 있음
    q = deque([(sr, sc, 0)])
    while q:
        r, c, is_break = q.popleft()

        if r == N - 1 and c == M - 1:
            return visit[r][c][is_break]

        for dr, dc in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                # 다음 칸이 0이고 아직 방문하지 않은 경우
                if mat[nr][nc] == "0" and not visit[nr][nc][is_break]:
                    visit[nr][nc][is_break] = visit[r][c][is_break] + 1
                    q.append((nr, nc, is_break))

                # 다음 칸이 1이고 아직 방문하지 않은 경우
                ## (벽을 부수고 지나가는 경우, is_break: 0 -> 1)
                elif mat[nr][nc] == "1" and not is_break:
                    visit[nr][nc][is_break + 1] = visit[r][c][is_break] + 1
                    q.append((nr, nc, is_break + 1))
    return -1


res = function(0, 0)
print(res)
