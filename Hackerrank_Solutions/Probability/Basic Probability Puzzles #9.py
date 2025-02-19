from fractions import Fraction

x,y,z=12,15,10

temp_X=Fraction(1,x)
temp_Y=Fraction(1,y)
temp_Z=Fraction(1,z)

temp_not_X=Fraction(x-1,x)
temp_not_Y=Fraction(y-1,y)
temp_not_Z=Fraction(z-1,z)

temp_XYZ=temp_not_X*temp_not_Y*temp_not_Z
flag = 1-temp_XYZ
print(flag)