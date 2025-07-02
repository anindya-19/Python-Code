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
    else:
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
    fp.write(equation + "=" + str(result) +"\n")
    fp.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input. Use format: number operator number (e.g 8 + 8 = 16)")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    calculatorFunction = operation_dict[op]
    result = calculatorFunction(num1,num2)