# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
	def __init__(self):
		self.balance=0
		
def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\nAmount Deposited:",amount)

def bankFees(self):
                self.balance = (95/100)*self.balance
        
    

def display(self):
                print("Account Number : " , self.accountNumber)
                print("Account Name : " , self.name)
                print("Account Balance : " , self.balance , " $")

def withdraw(self):
    amount = float(input("Enter amount to be Withdrawn: "))
    if self.balance>=amount:
	    self.balance-=amount
	    print("\n You Withdraw:", amount)
    else:
	    print("\n Insufficient balance ")

def display(self):
		print("\n Net Available Balance=",self.balance)


s = Bank_Account()

s.deposit()
s.withdraw()
s.display()
