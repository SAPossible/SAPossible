import heapq
import sys
input = sys.stdin.readline


# 다익스트라 + dp
V, E = map(int, input().split())
K = int(input())
nodes = [int(1e9)] * (V+1)
nodes[K] = 0

edges = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

heap = []
heapq.heappush(heap, (0, K))
while heap:
    # 현재노드, 현재 가중치합 pop
    w, v = heapq.heappop(heap)
    # 해당 노드 가중치가 가중치합 w보다 작은 경우 스킵
    if nodes[v] < w:
        continue

    # 현재노드와 연결된 다음노드 순회
    for nv, nw in edges[v]:
        # 가중치합 = 현재노드 가중치 + 다음노드 가중치
        total_w = w + nw
        # 가중치합이 다음노드 가중치합보다 작은 경우
        if total_w < nodes[nv]:
            # 노드 가중치 갱신
            nodes[nv] = total_w
            # 힙 추가
            heapq.heappush(heap, (total_w, nv))

for i in range(1, V+1):
    print(nodes[i] if nodes[i] != int(1e9) else 'INF')