#9 8 7 1
num = int(input("Enter the number: "))
if(1000<=num<=9999):
    d1=num//1000
    d2=(num//100)%10
    d3=(num//10)%10
    d4=num%10
    rev=0
    temp=num
    while(temp>0):
        rev=rev*10+temp%10
        temp//=10
    print(f"a. {d1} {d2} {d3} {d4}")
    print(f"b. {num} = {d1*1000} + {d2*100} + {d3*10} + {d4}")
    print(f"c. {rev}")

    
        