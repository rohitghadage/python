""" 1) while loop::;Write a program which uses a while loop to sum the squares of integers (starting from 1) until the total exceeds 200.
Print the final total and the last number to be squared and added."""

total=0
n=0
while ( total < 200 ):

    n=n+1
    total=total + ( n * n)
print("total=",total)
print(n)

"""2) for loop:::Write a program which finds the factorial of a given number. E.g. 3 factorial, or 3! is equal to 3 x 2 x 1; 5! is equal to 5 x 4 x 3 x 2 x 1, etc..
 Your program should only contain a single loop. """
x=int(input("enter the number to which calculate factorial"))
fact=1
i=1
for i in range(1,x+1):
    fact=fact * i
print("sum of factorial=",fact)

""" 3) do while loop:::  """