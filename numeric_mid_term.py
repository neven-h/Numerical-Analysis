import numpy as np
import matplotlib.pyplot as plt


# divided differences
def divdiff(x, y):
    # x : array of data points
    # y : array of y(x) data points

    c = np.copy(y)
    for k in range(1, len(x)):
        for i in range(len(x) - 1, k - 1, -1):
            c[i] = float(c[i] - c[i - 1]) / float(x[i] - x[i - k])
    return c


def interpoly(x, y):
    # Degree of polynomial
    c = divdiff(x, y)
    p = lambda k: sum([c[i] * np.prod([k - x[j] for j in range(i-1)]) for i in range(len(x))])
    
    return p, c


def vector(n):
    # arr = []
    x = []
    y = []
    for i in range(1, n + 1):
        x.append(-5 + 10 * ((i - 1) / (n - 1)))
        y.append((1 / (1 + x[i - 1] ** 2)))
    return x, y


x, y = vector(5)
p, c = interpoly(x, y)
#print(p, c)
x_example = np.linspace(-20, 20, 100)
y_example = p(x_example)
plt.plot(x_example, y_example, 'r')
plt.show()

# x,y = vector(10)
# print(p,c)
#
# p ,c = interpoly(x,y)
# x,y = vector(15)
# print(p,c)
#
# p ,c = interpoly(x,y)
# x,y = vector(20)
# print(p,c)


# for i in range(len(c)+1):
