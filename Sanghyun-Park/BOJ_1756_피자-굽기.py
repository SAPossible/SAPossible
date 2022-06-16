import sys


D, N = map(int, sys.stdin.readline().split())
oven = list(map(int, sys.stdin.readline().split()))
pizza = list(map(int, sys.stdin.readline().split()))

# 1. 실질적인 오븐을 표현
for d in range(1, D):
    oven[d] = min(oven[d], oven[d-1])

# 2. 최하단에서부터 순회를 시작하여 위치 가능 여부 판단
depth, p_idx = D, 0
for d in range(D-1, -1, -1):
    if p_idx == N:
        print(depth)
        break

    # 2.1. 오븐 지름이 피자 반죽의 지름보다 길거나 같다면, 위치 가능
    if oven[d] >= pizza[p_idx]:
        depth = d + 1
        p_idx += 1
else:
    # 3. 피자 반죽이 남아 있다면, "0" 출력
    print(0)
