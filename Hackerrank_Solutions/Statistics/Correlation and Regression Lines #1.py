import math

temp = -(3/4) 
flag=-(4/3)

# #  Temp and Flag are the Coefficients of the equation 3x+4y+8=0 and 4x+3y+7=0
# # Coefficients will tell how corelated the two lines are.
# # We are using Pearson Correlation Coefficient to find the correlation between the two lines.


r = math.sqrt(temp**2+flag**2)
r1=-temp%r
print(round(-r1,2))

#  - m1/root(m1^2+m2^2)



#  
