try:
    x = int(input("Please enter int value greater than zero"))
    print(x)
except ValueError:
    print("Input cannot be parsed as an integer")
