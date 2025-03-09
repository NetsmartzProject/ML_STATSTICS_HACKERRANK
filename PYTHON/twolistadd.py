list1=[2,4,6,8]
list2=[1,3,5,7]

temp=[list1+list2 for list1,list2 in zip(list1,list2)]

print(temp)