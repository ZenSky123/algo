x = "ABCABC"
y = "BCDBCD"

B = [['' for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
C = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]


def f(B, i, j, res=''):
    if i == 0 or j == 0:
        print(res[::-1])
        return
    if B[i][j] == '←':
        res += x[i - 1]
        f(B, i - 1, j - 1, res)
    elif B[i][j] == '↑':
        f(B, i - 1, j, res)
    else:
        f(B, i, j - 1, res)


def lcs(x, y):
    for i, xi in enumerate(x, start=1):
        for j, yj in enumerate(y, start=1):
            if xi == yj:
                C[i][j] = C[i - 1][j - 1] + 1
                B[i][j] = '←'
            elif C[i][j - 1] > C[i - 1][j]:
                C[i][j] = C[i][j - 1]
                B[i][j] = '↓'
            else:
                C[i][j] = C[i - 1][j]
                B[i][j] = '↑'
    f(B, len(x), len(y))


if __name__ == '__main__':
    lcs(x, y)
