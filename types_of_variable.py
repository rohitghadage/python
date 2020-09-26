# 1)instance-present init method
# 2)class or self-present inside class but outside the init method
class car:
    wheel=4
    def __init__(self):
        self.x=10
        self.y="bmw"


c=car()

car.wheel=5
print(c.x,c.y,c.wheel)
