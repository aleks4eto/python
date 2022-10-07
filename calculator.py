
#helper function deinitions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y

def displayMenu():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

def calculate(choiceVar ,num1Var, num2Var):
    if choice == '1': print(num1Var, "+", num2Var, "=", add(num1Var, num2Var))
    elif choiceVar == '2': print(num1Var, "-", num2Var, "=", subtract(num1Var, num2Var))
    elif choiceVar == '3': print(num1Var, "*", num2Var, "=", multiply(num1Var, num2Var))
    elif choiceVar == '4': print(num1Var, "/", num2Var, "=", divide(num1Var, num2Var))

next_calculation = "yes"
while next_calculation=="yes":
    displayMenu()
    choice = input("Enter choice(1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        calculate(choice, num1, num2)   

    else: print("Invalid Input")
    

    next_calculation = input("Let's do next calculation? (yes/no): ")
    while next_calculation != "yes" and next_calculation != "no":
        next_calculation = input("Invalid Input\nLet's do next calculation? (yes/no): ")
        
