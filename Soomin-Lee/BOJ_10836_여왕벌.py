import sys
input = sys.stdin.readline

M, N = map(int, input().split())
worms = [1] * (2 * M)

# 해당 수가 증가해야하는 시작 인덱스에 수를 배치
for _ in range(N):
    a, b, c = map(int, input().split())
    worms[a] += 1
    worms[a + b] += 1

cnt = 0
for k in range(2*M-1):
    worms[k] += cnt
    cnt = worms[k] - 1

for i in range(M - 1, -1, -1):
    print(*([worms[i]] + worms[M:-1]))