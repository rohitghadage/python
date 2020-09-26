"""class computer :
    def config(self):
        print("1tb,8 gb")
com=computer() #creation of object
computer.config(com) #calling a method using object
com.config() # another way to call method using using  object """

class employee:#creating of class
    id=339 # attributr / variables
    name="rohit"
    def display(self): # method
        print("id = {} \n name= {}".format(self.id,self.name)) # printing attribute
        print("id=%d\nname=%s"%(self.id,self.name)) #printring atttribute

emp=employee() # creating object
emp.display() # calling method using object

