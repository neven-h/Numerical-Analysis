import numpy as np
import matplotlib as plt


def divdiff(x, y):
    # x : array of data points
    # y : array of y(x) data points
    x.astype(float)
    y.astype(float)
    c = np.copy(y)
    for k in range(1, len(x)):
        for i in range(len(x) - 1, k - 1, -1):
            c[i] = float(c[i] - c[i - 1]) / float(x[i] - x[i - k])
    return c


def interpnewt(c, x, xnew):
    # Degree of polynomial
    p = c[n]
    ynew = []
    for i in range(len(xnew)):  # at every point of xnew
        for k in range(1,
                       len(x)):  # Calculate interp. recursively using Horner rule: p = c[n - k] + (xnew[i] - x[n - k]) * p
            ynew.append(p)
        return ynew


f1 = lambda x: x
f2 = lambda x: 1 / (1 + x ** 2)
i1 = (0, 5)
i2 = (0, 5)
for f, I in zip([f1, f2], [i1, i2]):
    N = np.array([i for i in range(1, 201)])
for i in range(200):
    n = N[i]



# plt.yscale('log')
# plot.plot(N, lin_errors)
# plot.plot(N, cheb_errors)
# plt.show()
