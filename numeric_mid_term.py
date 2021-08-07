import numpy as np
import matplotlib as plt

def divdiff(x, y):
    # x : array of data points
    # y : array of y(x) data points
    x.astype(float)
    y.astype(float)
    lenx = len(x)
    c = np.copy(y)
    for k in range(1, lenx):
        for i in range(lenx - 1, k - 1, -1):
            c[i] = float(c[i] - c[i - 1]) / float(x[i] - x[i - k])
    return c


# Q1B
def interpnewt(c, x, xnew):
    # n = len(x) - 1
    # Degree of polynomial
    p = c[n]
    ynew = []
    for i in range(len(xnew)):  # at every point of xnew
        for k in range(1,
                       len(x)):  # Calculate interp. recursively using Horner rule: p = c[n - k] + (xnew[i] - x[n - k]) * p
            ynew.append(p)
        return ynew


def cheb_points(a, b, n):
    p = np.array(range(n))
    p = np.cos(((2 * p + 1) * (np.pi)) / (2 * n))
    p = a + (b - a) * p * 0.5
    return p


def lin_points(a, b, n):
    return np.linspace(a, b, n)


f1 = lambda x: x
f2 = lambda x: 1 / (1 + x ** 2)
i1 = (0, 5)
i2 = (0, 10)
for f, I in zip([f1, f2], [i1, i2]):
    N = np.array([i for i in range(1, 201)])
lin_errors = [[] for i in range(200)]
cheb_errors = [[] for i in range(200)]
for i in range(200):
    n = N[i]



# plt.yscale('log')
# plot.plot(N, lin_errors)
# plot.plot(N, cheb_errors)
# plt.show()
