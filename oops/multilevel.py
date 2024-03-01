#multilevel inheritance
class Employees(): 
 
   def Name(self): 
       print("Employee Name: Arnav")
 
class salary(Employees):
   def Salary(self):
       print("Salary: 90000")
 
class Designation(salary):
   def desig(self):
       print("Designation: Developer")
 
call = Designation()
call.Name()
call.Salary()
call.desig()
