from fractions import Fraction
import math

temp=Fraction(1,3)
temp_x=Fraction(1,5)

temp_not=Fraction(1-temp)
temp_not_x=Fraction(1-temp_x)
P1=temp*temp_not_x
P2=temp_x*temp_not
flag=P1+P2

print(Fraction(flag))
