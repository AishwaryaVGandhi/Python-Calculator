import os


def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2
    
def multiplication(num1, num2):
    return num1 * num2
    
def division(num1, num2):
    return num1 / num2

operation_dict = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division
}

def calculator():
    first_num = float(input("Enter First Number : "))
    
    quit = True
    while quit:
        print("Operations : ", end = " ")
        for operator in operation_dict:
            print(operator, end = " ")
        operation = input("\nSelect Operation : ")
        
        next_num = float(input("Enter Next Number : "))
        
        calculator_function = operation_dict[operation]
        result = calculator_function(first_num, next_num)
        print(f"{first_num} {operation} {next_num} = {result}\n")
        
        print(f"Enter 'YES' to continue calculation with {result}.")
        print("Enter 'NEW' to new calculation.")
        print("Enter 'QUIT' to quit.\n")
        
        while True:
            choice = input().lower()
            
            if choice == "yes":
                first_num = result
            elif choice == "new":
                quit = False
                os.system("cls")
                calculator()
                return
            elif choice == "quit":
                quit = False
                print("You chose to quit. Bye !!")
                return
            else:
                print("Invalid Choice !! Enter 'YES' or 'NEW' or 'QUIT'.")
            

print("Python Calculator !!\n")    
calculator()
