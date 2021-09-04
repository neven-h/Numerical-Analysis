import numpy as np


# n = 6
x = np.ndarray((1, 3))
# n = 4
y = np.ndarray((1, 3))

# solution vector:  [-683.2628 -533.7413 1722.    ]

x[0:] = [-632.645354,  -494.191068 ,1594.449074]
y[0:] = [-683.2628 ,-533.7413, 1722. ]


e = x - y
e = abs(e)
print(np.max(e))
# print(e)
#
# for i in range(0, 3):
#     print(e[0][i])

    #print(e[0][i])


print("The answer for section d is: ", e[0][2])
# print("e: ", e)
