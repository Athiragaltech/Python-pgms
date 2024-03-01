class bank:  
    def __init__(self, name, bal,acno):  
        self.bal = bal  
        self.name = name
        self.acno=acno
  
    def display(self):  
        print("Account number: %d \nName: %s \nBalance: %d" % (self.bal, self.name,self.acno))  
  
  
emp1 = bank("Athira", 101,10000)  
emp2 = bank("Neethu", 102,2000)  
  
# accessing display() method to print employee 1 information  
  
emp1.display()  
  
# accessing display() method to print employee 2 information  
emp2.display() 
