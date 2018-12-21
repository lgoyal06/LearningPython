x =0
while x < 100:
        try:
            x = int(input('Please enter integer value'))
            if x<5:
                a=None
                a[3]=4
            elif x>5 and x <10:
                a=[0,1]
                a[2]=44
        except ValueError:
            print("Input cannot be parsed as an integer")
        except TypeError:
            print("Trying to use a None as a valid object")
        except IndexError:
            print("Straying from the bounds of the list")
        print("Program continues")
print("Program finished")
    
        
