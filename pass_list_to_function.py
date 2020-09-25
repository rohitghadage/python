list=[10,11,12,13,14,15]
def count(list):
    even=0
    odd=0
    for i in list:
        if i % 2 ==0:
            even+=1
        else:
            odd+=1
    print(even)
    print(odd)
count(list)

# to check string which is greater than 5
s={"rohit","vrj","vikram","tanaji","abcde"}
def check(s):
    count=0
    for i in s:
        if (len(i)>=5):
            count+=1
    print(count)
check(s)
