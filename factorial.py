"""n=int(input("enter the number which to be calculate fatorial of a number"))
fact=1
for i in range(1,n+1):
    fact=fact * i
print("factorial of num=",fact)  """

 # using recursion
n=int(input("enter the number which to be calculate fatorial of a number"))
def fact(n):
    if n==1 or n==0:
        return n
    else:
        return n*fact(n-1)
print("factorial=",fact(n))


