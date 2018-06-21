INF = 99999

m = [[0 for _ in range(100)] for _ in range(100)]
s = [[0 for _ in range(100)] for _ in range(100)]


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


if __name__ == '__main__':
    P = [
        10, 100, 5, 50
    ]
    print(RecurMatrixChain(P, 1, 3))
