import copy


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
stat_d = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]


def fill(tmp_mat, status, sr, sc):
    for stat in status:
        nr, nc = sr, sc
        while True:
            nr += dr[stat]
            nc += dc[stat]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                break
            elif tmp_mat[nr][nc] == 6:
                break
            elif tmp_mat[nr][nc] == 0:
                tmp_mat[nr][nc] = 9


def dfs(i, arr):
    global res
    # i: cctv index(depth)
    # d: cctv direction
    if i == len(cctvs):
        tmp_res = 0
        for r in range(N):
            tmp_res += arr[r].count(0)
        res = min(res, tmp_res)
        return

    # i번째 cctv 감시구역 fill
    tmp = copy.deepcopy(arr)
    cctv, r, c = cctvs[i]

    for s in stat_d[cctv]:
        fill(tmp, s, r, c)
        # [print(t) for t in tmp]
        # print()

        # 다음 cctv로
        dfs(i+1, tmp)
        tmp = copy.deepcopy(arr)


N, M = map(int, input().split())
mat = []
cctvs = []
for r in range(N):
    row = list(map(int, input().split()))
    mat.append(row)
    for c in range(M):
        if row[c] in [1,2,3,4,5]:
            cctvs.append((row[c], r, c))

res = int(1e9)
dfs(0, mat)
print(res)