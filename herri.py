class a:
    num1=int(input("Enter your first number:"))
    num2=int(input("Enter your Second number:"))
    def add(self):
        print("Do addition of two numbers",self.num1+self.num2)
    def subtraction(self):
        print("Do subtraction of two numbers:",self.num1-self.num2)

class b(a):
    def multy(self):
        print("Do multiplication of two numbers:",self.num1*self.num2)
    def divi(self):
        print("Do division of two numbers:",self.num1/self.num2)
    def rem(self):
        print("Do Reminder of two numbers:",self.num1%self.num2)
obj=b()
obj.add()
obj.subtraction()
obj.multy()
obj.divi()
obj.rem()



