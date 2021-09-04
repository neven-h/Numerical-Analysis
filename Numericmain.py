from mmn16a import GaussQnumberOne
from mmn16a import solveElimintaedSys
from mmn16a import SolveEquation
import numpy as np

n = 3
print("Section g. \n  n =", n)

A = np.ndarray((3, 3))
A[0, :] = [6.03, 1.99, 3.02]
A[1, :] = [4.16, -1.23, 1.27]
A[2, :] = [-4.81, -9.34, 0.987]
#A = ([[6.03, 1.99, 1], [4.16, -1.23, 1.27], [-4, 81, 9.34, 0.987]])

# A = np.array([[6.03, 1.99, 1], [4.16, -1.23, 1.27], [-4, 81, 9.34, 0.987]])
# T = np.array([1, 1, 1], [0, 1, 1], [0, 0, 1])
b = np.array([1, 1, 1])

# Extended matrix
M = np.c_[A, b]
S = np.c_[A, b]
Q = GaussQnumberOne(M, n)
X = solveElimintaedSys(Q, n)

print("source matrix: \n", S)
print("\n-----\n")
print(Q)
print("solution vector: ", X)


# n = 4
# y = solution vector:  [0.0293 0.0446 0.7345]

# n = 6
# x = solution vector:  [0.029329 0.044554 0.734483]

# n = 3
# [0.03 0.044 0.734]