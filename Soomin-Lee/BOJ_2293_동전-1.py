import sys

n, k = map(int, sys.stdin.readline().split())
coin_value = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for value in coin_value:
    for s in range(value, k + 1):
        dp[s] += dp[s - value]

print(dp[k])