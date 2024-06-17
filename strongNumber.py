# program to check whether the number is strong or not
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def is_strong(number):
    sumFactorial=0
    original=number
    while number>0:
        temp=number%10
        sumFactorial+=factorial(temp)
        number=number//10
    return original == sumFactorial

num=int(input("Enter the number to check whether the number strong or not "))
if is_strong(num):
    print("Strong number")
else:
    print("Not Strong ")