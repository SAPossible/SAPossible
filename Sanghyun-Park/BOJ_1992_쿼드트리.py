import sys


def compress(rs, cs, slen):
    color = IMAGE[rs][cs]
    flag = 0
    compressed = []

    for r in range(rs, rs+slen):
        for c in range(cs, cs+slen):
            if color != IMAGE[r][c]:
                compressed.append(compress(rs, cs, slen//2))
                compressed.append(compress(rs, cs+slen//2, slen//2))
                compressed.append(compress(rs+slen//2, cs, slen//2))
                compressed.append(compress(rs+slen//2, cs+slen//2, slen//2))
                flag = 1
                break
        if flag:
            break

    if compressed:
        return '(' + ''.join(compressed) + ')'
    else:
        return str(color)


N = int(sys.stdin.readline())
IMAGE = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

print(compress(0, 0, N))


"""
4
1111
1111
1111
1111

4
0000
0000
0000
0000

4
1100
1010
0101
0000

2
10
01
"""