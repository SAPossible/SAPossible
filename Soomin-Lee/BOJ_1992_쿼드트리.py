import sys

def packing(r, c, N):
    tmp = board[r][c]
    ans = ""
    flag = True

    for i in range(r, r+N):
        if not flag:
            break

        for j in range(c, c+N):
            if board[i][j] != tmp:
                ans += '('
                ans += packing(r, c, N//2)
                ans += packing(r, c + N//2, N//2)
                ans += packing(r + N // 2, c, N // 2)
                ans += packing(r + N // 2, c + N // 2, N // 2)
                ans += ')'
                flag = False
                return ans

    return tmp


N = int(sys.stdin.readline())
board = list(sys.stdin.readline().rstrip() for _ in range(N))

print(packing(0, 0, N))