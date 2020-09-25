""" # using recursion
 n=int(input("enter the number upto print fibbonacci series"))
def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-2) + fib(n-1)
i=0
for i in range(0,n+1):
    print(fib(i)) """

# without recursion
n=int(input("enter the number upto print fibbonacci series"))
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
     else:
        print(a)
        print(b)
    for i in range(2,n):
                 c=a+b
                a=b
                b=c
                print(c)
fib(n)
