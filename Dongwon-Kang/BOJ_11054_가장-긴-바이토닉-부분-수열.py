N = int(input())
A = list(map(int, input().split()))
A_reverse = A[::-1]
increase = [1] * N
decrease = [1] * N

for i in range(N):
    num = 1
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[j] + 1, increase[i])
        if A_reverse[i] > A_reverse[j]:
            decrease[i] = max(decrease[j] + 1, decrease[i])

res = 0
for k in range(N):
    res = max(increase[k] + decrease[::-1][k] - 1, res)
print(res)