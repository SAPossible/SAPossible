from collections import defaultdict

N, M = map(int, input().split())
shortcut = defaultdict(int)
for _ in range(N+M):
    x, y = map(int, input().split())
    shortcut[x] = y


res = 100//6
def bfs():
    global res
    visit = [1e9]*101
    q = [(1, 0)]

    while q:
        num, cnt = q.pop(0)
        # print(num, cnt, q)

        if cnt > res:
            continue
        if num >= 94:
            res = min(res, cnt)
            continue

        for i in range(6, 0, -1):
            if shortcut[num+i] > 0:
                next_num = shortcut[num+i]
            else:
                next_num = num+i

            if visit[next_num] > cnt+1:
                visit[next_num] = cnt+1
                q.append((next_num, cnt+1))

bfs()
print(res+1)