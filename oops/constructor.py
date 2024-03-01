#constructor
class Student:

    # constructor
    # initialize instance variable
    def __init__(self, name):
        self.name = name
       
    # instance Method
    def show(self):
        print('Object is created...!!')
        print('Hello, my name is', self.name)


# create object using constructor
s1 = Student('Arun')
s1.show()
