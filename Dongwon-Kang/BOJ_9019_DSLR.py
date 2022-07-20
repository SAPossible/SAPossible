import sys
from collections import deque


def bfs(A, B):
    register = [0]*10000
    register[A] = 1
    q = deque([(A, '')])

    while q:
        n, commands = q.popleft()

        if n == B:
            print(commands)
            return

        for d in ['D', 'S', 'L', 'R']:
            if d == 'D':
                nn = (n*2)%10000
            elif d == 'S':
                nn = (n-1)%10000
            elif d == 'L':
                nn = ((n*10)%10000) + n//1000
            elif d == 'R':
                nn = ((n%10)*1000) + n//10

            if not register[nn]:
                register[nn] = 1
                q.append((nn, commands+d))


T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    bfs(A, B)