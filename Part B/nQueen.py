def nQueen(n):
    matrix = [[0] * (n) for _ in range(n)]
    output

    def solve(matrix, n, x):
        if x == n:
            for i in matrix:
                print(*i)
            print()
            return

        for y in range(n):
            if isSafe(x, y, matrix, n):
                matrix[x][y] = 1
                solve(matrix, n, x + 1)
                matrix[x][y] = 0
        return

    solve(matrix, n, 0)