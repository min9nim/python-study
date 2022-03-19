def solution(seat):
    le = len(seat)
    result = [[0]*le]*le

    def mark(x, y, noMask):
        if x >= 0 and x < le and y >= 0 and y < le:
            c = seat[x][y]
            if c == '-':
                return
            if noMask and c == 'N':
                result[x][y] = 1
            else:
                result[x][y] = 1

    def traverse(x, y, noMask, d):
        mark(x-1, y, noMask)
        visit(x-1, y, d+1)
        mark(x+1, y, noMask)
        visit(x+1, y, d+1)
        mark(x, y-1, noMask)
        visit(x, y-1, d+1)
        mark(x, y-1, noMask)
        visit(x, y-1, d+1)

    def visit(x, y, d):
        if d > 3:
            return
        traverse(x, y, True if d == 3 else False, d)

    for i in range(le):
        for j in range(le):
            c = seat[i][j]
            if c == 'C':
                visit(i, j, 1)

    for str in seat:
        print(list(str))
    for arr in result:
        print(arr)

    return sum([sum(arr) for arr in result])


assert solution(
    ["M--NN-", "-M----", "-CC--M", "-N----", "N-M-C-", "-M----"]
) == 5
