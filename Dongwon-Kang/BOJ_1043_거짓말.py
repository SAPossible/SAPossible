N, M = map(int, input().split())
knows = set(input().split()[1:])
party = []

for _ in range(M):
    party.append(set(input().split()[1:]))

for _ in range(M):
    for p in party:
        if knows & p:
            knows = knows.union(p)

cnt = 0
for p in party:
    if knows & p:
        continue
    cnt += 1
print(cnt)