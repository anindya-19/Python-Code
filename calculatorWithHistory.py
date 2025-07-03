import os
HISTORY_FILE = "historyCalculator.txt"

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        print("Division by Zero is not possible")
        return None
    return a / b

operation_dict = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def showHistory():
    fp = open("HISTORY_FILE","r")
    lines = fp.readlines()
    if len(lines) == 0:
        print("No Histroy Found!!")
    else:
        for line in reversed(lines):
            print(line.strip())
        fp.close()

def clear_history():
    file = open("HISTORY_FILE","w")
    file.close()
    print("History Cleared Successfully!!")

def save_history(equation,result):
    fp = open("HISTORY_FILE","a")
    fp.write(f"{equation} = {result} \n")
    fp.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input. Use format: number operator number (e.g 8 + 8 = 16) or use the following Commands!")
        return
    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid Numbes. Please enter valid numbers! ")
        return

    if op not in operation_dict:
        print(f"Invalid Operator '{op}'. Use one of: {', '.join(operation_dict.keys())} ")
        return
    calculatorFunction = operation_dict[op]
    result = calculatorFunction(num1,num2)
    
    if result is not None:
        if int(result) == result:
            result = int(result)
        print("Result: ",result)
        save_history(user_input,result)
    
def main():
    print("____Calculator (type history, clear or exit)")
    while True:
        user_input = input("Enter calculations (+ - * /) or command (history, clear or exit):  ").strip().lower()
        
        if user_input == 'exit':
            print("Thanks For using! Have a nice day!")
            break
        elif user_input == 'history':
            showHistory()
        elif user_input == 'clear':
            os.system('cls')
            clear_history()
        else:
            calculate(user_input)

main()