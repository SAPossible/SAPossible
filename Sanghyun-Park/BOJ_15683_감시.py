import sys
from copy import deepcopy


def watch(row, col, dire, room):
    for d in dire:
        r, c = row, col
        while True:
            r, c = r + dy[d], c + dx[d]
            if 0 <= r < N and 0 <= c < M and room[r][c] != 6:  # 정상 범위 내에서 벽을 만나지 않았다면
                if room[r][c] == 0:  # 카메라가 위치하는 곳이 아니라면
                    room[r][c] = -1
            else:
                break


def monitor(room, step=0):
    global result

    if step == len(camera_loc):  # 모든 카메라의 방향 조정을 마쳤다면
        unwatched = 0
        for r in range(N):
            for c in range(M):
                if room[r][c] == 0:
                    unwatched += 1
        result = min(result, unwatched)
        return

    for dire in camera_dire[camera_loc[step][2]]:
        room_copied = deepcopy(room)
        watch(camera_loc[step][0], camera_loc[step][1], dire, room_copied)  # 감시 가능한 영역 기록
        monitor(room_copied, step+1)


dy = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dx = [0, 1, 0, -1]
camera_dire = [
    [],
    [[0], [1], [2], [3]],  # 1번 카메라를 90도씩 회전시킬 때, 가능한 모든 방향 조합
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]
camera_loc = []

N, M = map(int, sys.stdin.readline().split())  # input
ROOM = []
for r in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for c in range(M):
        if 1 <= row[c] <= 5:
            camera_loc.append((r, c, row[c]))  # 행, 열, 카메라 종류
    ROOM.append(row)

result = N * M
monitor(ROOM)  # DFS(기준: 카메라)

print(result)  # output
