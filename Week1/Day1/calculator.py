a = float(input("Enter the First Number:"))
b = float(input("Enter the Second Number:"))

operation = input("Enter the operator(+, -, *, /):")

if operation == "+":
    print("Result:", a+b)

elif operation == "-":
    print("Result:", a-b)

elif operation == "*":
    print("Result:", a*b)

elif operation == "/":
    if b!=0:
        print("Result:", a/b)
    else:
        print("Cannot divide by Zero")

else:
    print("Invalid Operator")

    