

# def Reverse(text):
#     return text[::-1]

def Reverse(text):
    for i in range(len(text)-1,-1,-1):
        print(text[i])

# text=input("Enter the text: ")

text=list(map(int,input("Enter the number: ").split()))

flag=Reverse(text)

print(flag)