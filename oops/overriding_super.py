#overriding
class parent:
    def f(self):
        print("This is parent class")
class child(parent):
    def f(self):
        super().f()
        print("Child class")
        
ob1 = child()
ob1.f()
