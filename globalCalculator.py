result = 0.0
arg1 = 0.0
arg2 = 0.0

def get_input():
    global arg1, arg2
    arg1 = eval(input("Enter first value"))
    arg2 = eval(input("Enter second value"))

def add():
    global result
    result = arg1 + arg2

def subtract():
    global result
    result = arg1 - arg2

def multiply():
    global result
    result = arg1 * arg2

def divide():
    global result
    result = arg1/arg2

def getResult():
    print(result)


def main():
    done = False
    while not done:
        print("Please enter operation")
        choice = input()
        if choice == 'A':
                get_input()
                add()
                getResult()
        elif choice == 'S':
                get_input()
                subtract()
                getResult()
        elif choice == 'D':
                get_input()
                divide()
                getResult()
        elif choice == 'M' :
                get_input()
                multiply()
                getResult()
        elif choice == 'Q' :
            done = True
        
        

main()
