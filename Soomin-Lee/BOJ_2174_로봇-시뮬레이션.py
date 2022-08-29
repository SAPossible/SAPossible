from collections import defaultdict

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
directions = ['E', 'N', 'W', 'S']

def rotating(dir, robot, order, order_cnt):
    cnt = int(order_cnt) % 4
    if order == 'L':
        next_direction = (directions.index(dir) + cnt) % 4
        direction[int(robot)][2] = directions[next_direction]

    else:
        next_direction = (directions.index(dir) - cnt) % 4
        direction[int(robot)][2] = directions[next_direction]


def moving(r, c, dir, robot, order_cnt):
    global result

    nd = directions.index(dir)

    for k in range(order_cnt):
        nr = r + dr[nd]
        nc = c + dc[nd]

        if nr < 0 or nr >= B or nc < 0 or nc >= A:
            result = 'Robot ' + robot + ' crashes into the wall'
            break

        elif land[nr][nc]:
            result = 'Robot ' + robot + ' crashes into robot ' + str(land[nr][nc])
            break

        r, c = nr, nc

    else:
        land[r][c] = int(robot)
        direction[int(robot)][0] = str(r+1)
        direction[int(robot)][1] = str(c+1)


A, B = map(int, input().split())
N, M = map(int, input().split())
result = 'OK'

land = [[0] * A for _ in range(B)]
direction = defaultdict(list)

# 로봇의 초기 위치, 방향
for k in range(N):
    x, y, d = input().split()
    land[int(y)-1][int(x)-1] = k+1
    direction[k+1] = [y, x, d]

# 로봇, 명령종류, 횟수
for _ in range(M):
    robot, order, order_cnt = input().split()
    r, c, dir = direction[int(robot)]
    if order == 'F':
        land[int(r)-1][int(c)-1] = 0
        moving(int(r)-1, int(c)-1, dir, robot, int(order_cnt))
        if result != 'OK':
            break
    else:
        rotating(dir, robot, order, order_cnt)

print(result)