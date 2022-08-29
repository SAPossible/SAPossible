import sys


N, K = map(int, sys.stdin.readline().split())
COINS = [int(sys.stdin.readline()) for _ in range(N)]

dp = [1] + [0] * K
for coin in COINS:
    for value in range(coin, K+1):
        dp[value] += dp[value-coin]

print(dp[K])
