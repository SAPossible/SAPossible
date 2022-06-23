import sys
import heapq


N = int(sys.stdin.readline())
COURSES = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)])
# print(f'N: {N} -> input result: {COURSES}')

rooms = [COURSES[0][1]]
for i in range(1, N):
    if rooms[0] > COURSES[i][0]:
        heapq.heappush(rooms, COURSES[i][1])
        # print(f'when another room is needed: {rooms}')
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, COURSES[i][1])
        # print(f'when able to success: {rooms}')

print(len(rooms))
