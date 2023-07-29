class Student:
   def check_pass_fail(self):
      if self.marks>=40:
         return True
      else:
         return False
         
Object1=Student()
Object1.name="Santosh"
Object1.age=23
Object1.address="Miklajung"
Object1.marks=85
did_pass=Object1.check_pass_fail()
print(did_pass)

print(Object1.name)
print(Object1.marks)

Object2=Student()
Object2.name="Binod"
Object2.marks=30
did_pass=Object2.check_pass_fail()
print(did_pass)