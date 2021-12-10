class Atm(object):
    def __init__(self,bankBalance,cardNumber,pinNumber):
        
        
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.bankBalance=bankBalance
    
    def balance(self):
        print('THE MONEY IN YOUR ACCOUNT IS ',self.bankBalance)
    def withdrawl(self):
        withdrawl=int(input('ENTER THE MONEY YOU WANT TO WITHDRAW '))
        print('YOU WITHDREW ',withdrawl)
        self.bankBalance-=withdrawl
    def getcardNumber(self):
        
        print('YOUR CARDNUMBER IS ',self.cardNumber)
    def getpinNumber(self):
        
        print('YOUR PIN IS ',self.pinNumber)

account1=Atm(25000,'4567','1234')
account1.balance()
account1.withdrawl()
account1.balance()
account1.getcardNumber()        
account1.getpinNumber()