N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]


def open_boundary(sr, sc):
    global is_moved
    q = [(sr, sc)]
    united_nations = [(sr, sc)]
    united_pop = nations[sr][sc]

    while q:
        r, c = q.pop(0)
        visit[r][c] = 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]\
                    and L <= abs(nations[r][c] - nations[nr][nc]) <= R:
                visit[nr][nc] = 1
                q.append((nr, nc))
                united_nations.append((nr, nc))
                united_pop += nations[nr][nc]
    if len(united_nations) > 1:
        is_moved = True
        for ur, uc in united_nations:
            nations[ur][uc] = int(united_pop / len(united_nations))

cnt = 0
is_moved = True
while is_moved:
    is_moved = False
    visit = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                open_boundary(r, c)

    if is_moved:
        cnt += 1
    else:
        break
print(cnt)
