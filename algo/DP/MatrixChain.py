INF = 99999

n = 4
m = [[0 for _ in range(n)] for _ in range(n)]
s = [[0 for _ in range(n)] for _ in range(n)]


def RecurMatrixChain(P, i, j):
    if i == j:
        m[i][j] = 0
        s[i][j] = i
        return m[i][j]
    m[i][j] = INF
    s[i][j] = i
    for k in range(i, j):
        q = RecurMatrixChain(P, i, k) + RecurMatrixChain(P, k + 1, j) + P[i - 1] * P[k] * P[j]
        if q < m[i][j]:
            m[i][j] = q
            s[i][j] = k
    return m[i][j]


def MatrixChain(P, n):
    result = 0
    for r in range(2, n + 1):
        for i in range(1, n - r + 2):
            j = i + r - 1

            m[i][j] = m[i + 1][j] + P[i - 1] * P[i] * P[j]
            s[i][j] = i
            for k in range(i + 1, j):
                t = m[i][k] + m[k + 1][j] + P[i - 1] * P[k] * P[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k
                    result = m[i][j]
    return result


if __name__ == '__main__':
    P = [
        10, 100, 5, 50
    ]
    # print(RecurMatrixChain(P, 1, n-1))
    print(MatrixChain(P, 3))
