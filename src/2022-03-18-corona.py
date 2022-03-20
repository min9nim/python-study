def solution(seat):
    le = len(seat)
    result = [[0]*le for _ in range(le)]

    for arr in result:
        print(arr)

    def visit(x, y, d):
        if 0 <= x < le and 0 <= y < le:
            c = seat[x][y]
            if c != '-' and c != 'C':
                if d < 3 or (d == 3 and c == 'N'):
                    result[x][y] = 1

            if d < 3:
                visit(x-1, y, d+1)
                visit(x+1, y, d+1)
                visit(x, y-1, d+1)
                visit(x, y+1, d+1)

    for i in range(le):
        for j in range(le):
            c = seat[i][j]
            if c == 'C':
                visit(i-1, j, 1)
                visit(i+1, j, 1)
                visit(i, j-1, 1)
                visit(i, j+1, 1)

    for str in seat:
        print(list(str))
    for arr in result:
        print(arr)

    return sum([sum(arr) for arr in result])


assert solution(
    ["M--NN-", "-M----", "-CC--M", "-N----", "N-M-C-", "-M----"]
) == 5


print('done')
