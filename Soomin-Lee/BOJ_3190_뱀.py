from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]  
dc = [1, 0, -1, 0]

def playing(r, c, direction):
    global time

    queue = deque([(r, c)])
    snakes[r][c] = 2
    nr, nc = 0, 0

    while True:
        nr, nc = nr + dr[direction], nc + dc[direction]
        time += 1

        if len(changes):
            if time == int(changes[0][0]):
                t, nd = changes.popleft()

                if nd == 'L':
                    direction = (direction + 3) % 4
                else:
                    direction = (direction + 1) % 4

        if 0 <= nr < N and 0 <= nc < N:
            if snakes[nr][nc] == 1:
                queue.append((nr, nc))
                snakes[nr][nc] = 2

            elif snakes[nr][nc] == 0:
                snakes[nr][nc] = 2
                queue.append((nr, nc))
                br, bc = queue.popleft()
                snakes[br][bc] = 0

            elif snakes[nr][nc] == 2:
                break

        else:
            break


N = int(input())
K = int(input())
snakes = [[0] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    snakes[r-1][c-1] = 1

L = int(input())
changes = deque()
for _ in range(L):
    X, C = input().split()
    changes.append((X, C))

time = 0

playing(0, 0, 0)

print(time)