class Student:
    def check_pass_fail(self):
        if self.marks>=40:
            return True
        else:
            return False
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

Object1=Student("Santosh",85)
Object2=Student("Kiran",30)
print(Object1.name)
print(Object1.marks)
print(Object2.name)
print(Object2.marks)

did_pass=Object1.check_pass_fail()
print(did_pass)
did_pass=Object2.check_pass_fail()
print(did_pass)