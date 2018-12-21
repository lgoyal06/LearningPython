#Encapsulation of variables by restricting its scope to private
class Rational:
    def __init__(self,n,d):
        self.__numerator=n
        if d != 0:
            self.__denominator=d
        else:
            print("Attempt to make an illegal rational number")
            from sys import exit
            exit(1)
    def set_numerator(self,n):
        self.__numerator = n
        
    def set_denominator(self,d):
        if d !=0:
            self.__denominator=d
        else:
            print("Attempt to make an illegal rational number")
            from sys import exit
            exit(1)

    def get_numerator(self):
        return self.__numerator
        
    def get_denominator(self):
        return self.__denominator

    def __str__(self):
        return str(self.get_numerator()/self.get_denominator())
            
            
def main():
    frac1= Rational(2,3)
    print(frac1)
    print(frac1.__denominator)
    frac2= Rational(2,0)
    print(frac2)
    
main()
