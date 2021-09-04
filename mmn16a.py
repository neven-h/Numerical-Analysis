import numpy as np

def round_sig(x, sig):
    return round(x, sig)


def GaussQnumberOne(M, n):
    for i in range(0, len(M) - 1):
        GaussStep(M, i, i, n)
    return M


def GaussStep(M, r, c, n):
    m = 1
    for i in range(r + 1, len(M)):
        # print(M[i], "M[i]")
        # print("aaa", M[i][c], type(M[i][c]))
        m = M[i][c] / M[r][c]
        m = round_sig(m, n)
        M[i][c] = 0
        for j in range(c + 1, len(M[0])):
            M[i][j] = M[i][j] - round_sig(M[r][j] * m, n)
            M[i][j] = round_sig(M[i][j], n)
    return M


def solveElimintaedSys(E, n):
    x = np.zeros(len(E[0]) - 1)
    for r in range(len(E) - 1, -1, -1):
        SolveEquation(E[r], x, r, n)
    return x


def SolveEquation(e, x, r, n):
    add = 0
    sum = 0
    answer = 0
    for i in range(len(e) - 2, r, -1):
        # print("ei", e[i])
        # print("xi", x[i])
        add = add + e[i] * x[i]
    sum = e[len(e) - 1] - add
    answer = round_sig(sum / e[r], n)
    x[r] = answer
