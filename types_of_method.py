# three types of method
# 1)instance-which is related to the instance variable
# 2)class-which is related to the class(static) varible  use @classmethod
# 3)static-which is not related to instance nor class.it is directly releted to class use @staticmethod

class employee:
    company="capjemini"
    def __init__(self,id,name):
        self.id=id
        self.name="rohit"

    @classmethod
    def c_name(cls):
        return cls.company

    @staticmethod
    def m_name():
        print("I am rohit")
e=employee(339,"rohit")
print(e.id,e.name)
print(employee.c_name())
print(employee.m_name())