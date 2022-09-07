from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    global flag

    visited = [0] * N
    visited[start] = 1
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == end:
            flag = True
            return

        for w in range(N):
            if board[node][w] and not visited[w]:
                visited[w] = 1
                queue.append(w)


N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
route = list(map(int, input().split()))

for k in range(M-1):
    flag = False
    bfs(route[k]-1, route[k+1]-1)

    if not flag:
        print('NO')
        exit()

else:
    print('YES')