"""" # map function: syntax: map(fun,iter)
num=["10","20","30"]
num=list(map(int,num))
#print(num[1])
x=10+num[1]
print(x)"""


# without lambda

num=[1,2,3,4]
square=list(map(lambda a:a*a,num))
print(square)



""" # using lambda
num=[1,2,3,4]
square=list(map(lambda a:a*a,num))
print(square)
"""