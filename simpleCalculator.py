def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations_dict = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}

num1 = int(input("Enter the first number: "))
print("Available Operations: ")
for keys in operations_dict:
    print(keys)
while True:
    operator = input("Enter what Operation you want to perform:  ")
    num2 = int(input("Enter the second number: "))
    calculatorFunction = operations_dict[operator]
    output = calculatorFunction(num1,num2)
    print(f"{num1} {operator} {num2} = {output}")

    choice = input(f"Enter 'y' to continue to continue previous operaion with {output} or 'n' to exit ").strip().lower()

    if choice == 'y':
        num1 = output
    else:
        print("Bye!!")
        break
    
    
