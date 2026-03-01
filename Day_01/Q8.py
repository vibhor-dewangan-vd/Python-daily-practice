#count number of digits
##34564
def count_digits(num):
    if num==0:
        return 1
    count=0
    num=abs(num)
    while(num>0):
        count=count+1
        num//=10
    return count
num = int(input("Enter the number: "))
print(f"Total digits : {count_digits(num)}")
        
