from fractions import Fraction
import math
temp =10
flag =math.factorial(temp-1)
temp_x = math.factorial(temp-2)
sitting_together=temp_x*2

print(Fraction(sitting_together,flag))

