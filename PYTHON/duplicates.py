
def duplicates(numbers):
    seen = set()
    duplicates = set()
    
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
            
    return list(duplicates)
    
        # count=0
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]==numbers[j]:
        #             count+=1
        #             return count
        # return 0    
    
numbers = list(map(int, input("Enter numbers: ").split()))
flag = duplicates(numbers)
print(flag)