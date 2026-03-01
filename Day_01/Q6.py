#Reverse of a number
def reverse_num(num):
    rev=0
    while(num>0):
        rev=rev*10+num%10
        num=num//10
    return rev
num=int(input("Enter the number: "))
result=reverse_num(num)
print(f"Reversed number : {result} ")