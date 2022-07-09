from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def bfs(k, v):
    cnt = 0
    visited = [0] * (N + 1)
    visited[v] = 1
    queue = deque([v])

    while queue:
        tmp = queue.popleft()
        for next, usado in graph[tmp]:
            if usado >= k and not visited[next]:
                visited[next] = 1
                queue.append(next)
                cnt += 1
    return cnt

N, Q = map(int, input().split())
graph = defaultdict(list)

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v))

