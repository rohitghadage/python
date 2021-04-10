# . You are given a number ‘N’. Your task is to find all the numbers ranging from 1 to N with the
# fact that absolute difference between consecutive digits of a number is 1.
# Input format:
# Input contains integer N
# Output format:
# Output displays all the numbers that satisfy the given condition and ‘-1’ if no number is
# present.
# Sample Testcases:
# Input 1
# 30
# Output 1
# 10 12 21 23
# Input 2
# 9
# Output 2
# -1


n = int(input())

for i in range(10,n):
    if(n<=9):
        print("-1")

    else:
        if(n<100):
            n1 = i%10
            n2 = i//10

            diff = abs(n1 - n2)
            #print(diff)
            
            if(diff == 1):
                print(i)

        else:
            print("invalid number")