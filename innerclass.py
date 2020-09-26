class student:
    def __init__(self,name,roll_no):
        self.x=name
        self.y=roll_no
        self.lap=self.laptop("i3","8gb","1tb")
    def show(self):
        print("name={}\nroll_no={}".format(self.x,self.y))
        self.lap.show()
    class laptop:
        def __init__(self,pro,ram,hd):
            self.a=pro
            self.b=ram
            self.c=hd
        def show(self):
            print("pro={}\nram={}\nhd={}".format(self.a,self.b,self.c))

s=student("rohit",339)
s.show()

