def quad(sr, sc, er, ec, start):
    for r in range(sr, er):
        for c in range(sc, ec):
            # print('r:', r, 'c:', c)
            if mat[r][c] != start:
                print('(', end='')
                nr = (er-sr)//2
                nc = (ec-sc)//2
                quad(sr, sc, er-nr, ec-nc, mat[sr][sc])
                quad(sr, sc+nc, er-nr, ec, mat[sr][sc+nc])
                quad(sr+nr, sc, er, ec-nc, mat[sr+nr][sc])
                quad(sr+nr, sc+nc, er, ec, mat[sr+nr][sc+nc])
                print(')', end='')
                return
    print(start, end='')


N = int(input())
mat = [list(map(int, input())) for _ in range(N)]
quad(0, 0, N, N, mat[0][0])