# Sum of Digits (3-digit number)
# Accept a 3-digit number and:
# Print each digit separately
# Find the sum of digits
# Example:
# Input: 456
# Output: 4 + 5 + 6 = 15
def sum_of_digits():
    num=int(input("Enter 3-digit number : "))
    if 100<=num<=999:
        d1=num//100
        d2=(num//10) %10
        d3=num%10
        d1+d2+d3
        print(f"{d1}+{d2}+{d3}")
    else:
        print("Invalid Number")
sum_of_digits()