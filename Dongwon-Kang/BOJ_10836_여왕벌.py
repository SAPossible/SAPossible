M, N = map(int, input().split())

worms = [1] * (2*M-1)
for _ in range(N):
    zero, one, two = map(int, input().split())
    for i in range(zero, zero+one):
        worms[i] += 1
    for j in range(zero+one, 2*M-1):
        worms[j] += 2

for k in range(M-1, -1, -1):
    print(*([worms[k]]+worms[M:]))