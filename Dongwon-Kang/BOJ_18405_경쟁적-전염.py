N, K = map(int, input().split())
mat = []
virus = []
for r in range(N):
    mat.append(list(map(int, input().split())))
    for c in range(N):
        if mat[r][c]:
            virus.append((mat[r][c], r, c))
s, x, y = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
virus.sort()
q = virus
for _ in range(s):
    for _ in range(len(q)):
        v, r, c = q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<N and 0<=nc<N and not mat[nr][nc]:
                mat[nr][nc] = v
                q.append((v, nr, nc))

print(mat[x-1][y-1])