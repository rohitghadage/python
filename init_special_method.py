#__init__  method same work as constructor

class employee:
    def __init__(self,id,name):
        self.x=id
        self.y=name
    def display(self):
       # print("id={} \n name={}".format(self.x,self.y))
        print("id=%d\nname=%s" %(self.x,self.y))
emp=employee(339,"rohit")
emp.display()
