# Description: Fibonacci series using recursion
# F(n) =F(n-1)+F(n-2) for n>1

# where :
#     F(0)=0
#     F(1)=1

def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci(i),end=" ")