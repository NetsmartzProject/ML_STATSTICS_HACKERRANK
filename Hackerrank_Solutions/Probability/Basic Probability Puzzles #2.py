# Basic Probability Puzzles #2


from fractions import Fraction

count=0
temp =6*6
for i in range(1,6):
    for j in range(1,6):
        if(i!=j) and (i+j)==6:
            count+=1
print(Fraction(count,temp))
