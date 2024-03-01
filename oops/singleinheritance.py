
# single inheritance

class Parent:
	def func1(self):
		print("This  is  parent class.")
# Derived class

class Child(Parent):
	def func2(self):
		print("This  is  child class.")

object = Child()
object.func1()
object.func2()
