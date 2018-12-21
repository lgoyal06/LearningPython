class RationalNum:
    def __init__(self,num,dem):
        self.numerator=num
        if dem == 0:
            print("Denominator sould not be zero")
            from sys import exit
            exit(1)
        self.denominator=num
fract = RationalNum(1,1)
print(fract.numerator)
