num1=float(input("Enter the number:"))
num2=float(input("Enter the number:"))
operator=input("Enter the operaor:")

if operator =="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("Invalid Operator!")

