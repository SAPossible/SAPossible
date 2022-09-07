import sys
input = sys.stdin.readline

def count_length(node, s):
    queue = [node]
    cnt = 1

    while True:
        tmp = []
        for q in queue:
            if graph[q]:
                for w in graph[q]:
                    tmp.append(w)
        if s in tmp:
            break
        queue = tmp
        cnt += 1

    return cnt


N = int(input())
graph = [[] for _ in range(N+1)]
cnt = [0] * N

while True:
    s, e = map(int, input().split())
    if s == -1 and e == -1:
        break

    graph[s].append(e)
    graph[e].append(s)

for k in range(1, N+1):
    ret = [0] * N
    for s in range(1, N+1):
        if k != s:
            answer = count_length(k, s)
            ret[s-1] = answer
    cnt[k-1] = max(ret)

ret = 0
answer = []
min_value = min(cnt)
for idx, c in enumerate(cnt):
    if c == min_value:
        ret += 1
        answer.append(idx+1)

print(min_value, ret)
print(*answer)