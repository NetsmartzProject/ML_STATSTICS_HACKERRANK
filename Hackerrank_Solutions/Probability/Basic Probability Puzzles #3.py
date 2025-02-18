# Basic Probability Puzzles #3

# Enter your code here. Read input from STDIN. Print output to STDOUT   
from fractions import Fraction

temp_X=7
temp_Y=9
temp_Z=8

RED_X,RED_Y,RED_Z=4,5,4

BLACK_X,BLACK_Y,BLACK_Z=3,4,4

P_R_X = RED_X/temp_X
P_B_X=BLACK_X/temp_X

P_R_Y=RED_Y/temp_Y
P_B_Y=BLACK_Y/temp_Y

P_B_Z=BLACK_Z/temp_Z
P_R_Z=RED_Z/temp_Z

P1 = P_R_X * P_R_Y * P_B_Z
P2 = P_R_X * P_B_Y * P_R_Z
P3 = P_B_X * P_R_Y * P_R_Z

temp = P1+P2+P3
print(temp)