

#  To finding the the mean of two equation we need to find the intersection point of the two lines.

import numpy as np

temp=np.array([[4,-5],[20,-9]])
flag=np.array([-33,107])

solution = np.linalg.solve(temp, flag)

mean_x=map(int,solution)
print(*mean_x)

# CAN ALSO BE DONE BY USING determinant method (Cramer's Rule), but it is not efficient for large number of equations.

# Given coefficients
a1, b1, c1 = 4, -5, -33
a2, b2, c2 = 20, -9, 107

# Determinants
D = (a1 * b2) - (b1 * a2)
Dx = (c1 * b2) - (b1 * c2)
Dy = (a1 * c2) - (c1 * a2)

# Solving for x and y
x = Dx // D  # Integer division
y = Dy // D  # Integer division

# Output the results
print(x, y)
