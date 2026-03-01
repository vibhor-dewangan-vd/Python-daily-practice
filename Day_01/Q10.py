#  Write A Program which is taking 5 int value and calculate sum of cube of all numbers [Write cube
# function]
def sum_of_cube(n1,n2,n3,n4,n5):
    return (n1**3)+(n2**3)+(n3**3)+(n4**3)+(n5**3)
    
num1= int(input("Enter the 1st number: "))
num2= int(input("Enter the 2nd number: "))
num3= int(input("Enter the 3rd number: "))
num4= int(input("Enter the 4th number: "))
num5= int(input("Enter the 5th number: "))

result= sum_of_cube(num1,num2,num3,num4,num5)
print(f"Sum of Cubes : {result}")
