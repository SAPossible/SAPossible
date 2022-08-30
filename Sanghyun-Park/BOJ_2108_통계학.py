import sys
from collections import Counter


N = int(sys.stdin.readline())
NUMS = [int(sys.stdin.readline()) for _ in range(N)]
NUMS_counted = [(key, val) for key, val in Counter(NUMS).items()]
NUMS_counted.sort(key=lambda x: (-x[1], x[0]))
# print(NUMS_counted)

print(round(sum(NUMS)/N))
print(sorted(NUMS)[N//2])
if len(NUMS_counted) >= 2 and NUMS_counted[0][1] == NUMS_counted[1][1]:
    print(NUMS_counted[1][0])
else:
    print(NUMS_counted[0][0])
print(max(NUMS)-min(NUMS))
