import sys

N, R, C = map(int, sys.stdin.readline().split())

result = 0
while N > 0:
    N -= 1
    leng = 2 ** N

    if R < leng and C < leng:
        result += 0
    elif R < leng and C >= leng:
        result += leng ** 2
        C -= leng
    elif R >= leng and C < leng:
        result += 2 * leng ** 2
        R -= leng
    else:
        result += 3 * leng ** 2
        R -= leng
        C -= leng

print(result)
