import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        print("Error: Division by zero is not possible")
    return a/b

operations_dict = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Please enter a valid integer")
    print("Available Operations: ")
    for keys in operations_dict:
        print(keys)
    continueFlag = True
    while continueFlag:
        operator = input("Enter what Operation you want to perform:  ").strip()
        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter a valid integer")
        calculatorFunction = operations_dict[operator]
        output = calculatorFunction(num1,num2)
        if output is not None:
            print(f"{num1} {operator} {num2} = {output}")
        else:
            continue #division by zero case, ask for the second number again

        choice = input(f"Enter 'y' to continue to continue previous operaion with {output} or 'n' to start a new calculation or 'x' to exit : ").strip().lower()

        if choice == 'y':
            num1 = output
        elif choice == 'x':
            print("Bye!!")
            continueFlag = False
        elif choice == 'n':
            continueFlag = False
            print("Starting a new Calculation!")
            os.system('cls')
            calculator()
        else:
            print("Please enter a valid choice!")


calculator()
        
    
    
