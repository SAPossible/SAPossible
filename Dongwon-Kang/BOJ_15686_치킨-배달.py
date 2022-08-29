from itertools import combinations


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
res = 1e9
house = []
chicken = []

for r in range(N):
    for c in range(N):
        if mat[r][c] == 1:
            house.append((r, c))
        elif mat[r][c] == 2:
            chicken.append((r, c))

for chicken_lst in combinations(chicken, M):
    dist = 0
    for house_r, house_c in house:
        tmp_dist = 1e9
        for chicken_r, chicken_c in chicken_lst:
            tmp = abs(chicken_r - house_r) + abs(chicken_c - house_c)
            tmp_dist = min(tmp_dist, tmp)
        dist += tmp_dist
    res = min(res, dist)
print(res)