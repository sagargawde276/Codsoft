print("Welcome to the calculator")
print("Select the operation")
print("1. Add")
print("2. Subtract")
print("3. multiple")
print("4. Divide")

choice = input("Enter the operaion number:")

if choice in ['1', '2', '3', '4' ]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print(f"{num1}+{num2}={num1+num2}")

    elif choice == '2':
        print(f"{num1}-{num2}={num1-num2}")  

    elif choice == '3':
        print(f"{num1}*{num2}={num1*num2}")

    elif choice =='4':
        if num2 !=0:
            print(f"{num1}/{num2}={num1/num2}")  
        else:
            print("Error! Divison by zero")

else:
    print("Invalid input")            