

# m= r * standard deviation of the dependent variable/standard deviation of the independent variable

import math

Mean_P=100
Deviation_P=8
Mean_S,Deviation_S=103,4
r_squared = 0.4

temp=math.sqrt(r_squared)
temp1=round(temp,3)
flag=Deviation_P/Deviation_S
m = temp1 * flag
print(round(m,2))