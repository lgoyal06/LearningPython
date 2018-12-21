class BankAccount:
    def __init__(self,number, aadhar, name, balance):
        self.__account_number=number
        self.__masked_aadhar=aadhar*4
        self.__name=name
        self.__balance=balance
        
    def deposite(self, money):
        if money<=0:
            print("Minimum of 1 rupees should be deposited")
            return False
        else:
            self.__balance+=money
            return True

    def withdraw(self,money):
        if self.__balance<money:
            print("Insufficient Balance")
            return False
        else:
            self.__balance-=money
            return True
        
    def balanceCheck(self):
        return round(self.__balance,2)
            
def main():
    account_1=BankAccount(1212,121212,'Lalit',23.38)
    print(account_1.balanceCheck())
    account_1.withdraw(23)
    print(account_1.balanceCheck())
    account_1.deposite(21)
    print(account_1.balanceCheck())
main()
        
