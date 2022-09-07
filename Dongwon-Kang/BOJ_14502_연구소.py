from collections import deque
import copy


N, M = map(int, input().split())
res = 0
mat = []
virus = []
for r in range(N):
    tmp_lst = list(map(int, input().split()))
    mat.append(tmp_lst)
    for c in range(M):
        if tmp_lst[c] == 2:
            virus.append((r, c))

def count_zero():
    global res
    tmp_mat = copy.deepcopy(mat)
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0<=nr<N and 0<=nc<M and tmp_mat[nr][nc] == 0:
                tmp_mat[nr][nc] = 2
                q.append((nr, nc))
    cnt = 0
    for m in tmp_mat:
        cnt += m.count(0)
    res = max(res, cnt)
    # print(cnt)
    # [print(t) for t in tmp_mat]


def make_wall(cnt):
    if cnt == 3:
        count_zero()
        return
    for r in range(N):
        for c in range(M):
            if mat[r][c] == 0:
                mat[r][c] = 1
                make_wall(cnt+1)
                mat[r][c] = 0


make_wall(0)
print(res)