class student:
    def check_pass_fail(self):
        if self.marks >=40:
            return True
        else:
            return False
student1=student()
# student2=student()
student1.name="Santosh"
student1.marks=89
# print(student1.name)
# print(student1.marks)
did_pass=student1.check_pass_fail()
print(did_pass)
student2=student()
student2.name="Ram"
student2.marks=30
did_pass=student2.check_pass_fail()
print(did_pass)