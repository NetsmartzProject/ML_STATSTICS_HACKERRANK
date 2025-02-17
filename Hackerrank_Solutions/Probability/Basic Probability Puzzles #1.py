from fractions import Fraction

# We use Fraction Form to get the exact value of the probability.

# In the two-argument form of the constructor, Fraction(8, 6) will
# produce a rational number equivalent to 4/3. Both arguments must
# be Rational. The numerator defaults to 0 and the denominator
# defaults to 1 so that Fraction(3) == 3 and Fraction() == 0.

temp=6*6
count=0
for i in range(1,7):
    for j in range(1,7):
        if (i+j) <= 9:
            count+=1

print(Fraction(count,temp))          
