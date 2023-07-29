class employee:
    company="Apple"
    def show(self):
        print("f the name is the {self.name} company is {self.company}")
    def changeCompany(Cls,newCompany):
        Cls.company=newCompany
        e1=employee()
        e1.name="Santosh"
        e1.changeCompany("Tesla")
        e1.show()
