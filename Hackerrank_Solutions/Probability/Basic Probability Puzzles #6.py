from fractions import Fraction


bag_1_white,bag_1_black=5,4
bag_2_white,bag_2_black=7,6

total_bag_1=bag_1_white+bag_1_black
total_bag_2=bag_2_white+bag_2_black+1

temp= Fraction(bag_1_white,total_bag_1)
temp1=Fraction(bag_2_black,total_bag_2)

flag=Fraction(bag_1_black,total_bag_1)
flag1=Fraction(bag_2_white,total_bag_2)

P1=(temp*temp1)
P2=(flag*flag1)

Pfinal=Fraction(P1+P2)
print(Pfinal,"pfinal")
