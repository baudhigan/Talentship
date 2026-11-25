def factorial(n):
    fact=1

    for i in range(1, n+1):
        fact = fact*i
    
    return fact

number = int(input("Enter the number:"))

if number<=0:
    print("Invalid Number")
else:
    result = factorial(number)
    print("Factorial = ", result)
    