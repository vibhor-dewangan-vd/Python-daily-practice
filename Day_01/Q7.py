#palindrome of a number check
def palindrome_check(num):
    rev=0
    temp=num
    while(temp >0):
        rev=rev*10+temp%10
        temp//=10
    return rev==num
num = int(input("Enter the number: "))
if palindrome_check:
    print(f"{num} is Palindrome")
else:
    print(f"{num} is NOT a palindrome")
