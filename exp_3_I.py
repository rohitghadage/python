'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

# name:Rohit vinayak Ghadage
# Roll_no:322
# URN:18131048
# Assignment_No:3
# You are given a number N and following by an array of N numbers and followed by two
# elements U and V. Find the minimum distance between the elements U and V in the array.
# The array may have duplicates.
# For example, if the array is (1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9)
# Minimum distance (U=4, V=7): 4
# Input Format:
# First Line contains integer representing number of elements N.
# Second line contains N elements separated by spaces.
# Third line contains two numbers separated by spaces representing U and V.
# Output Format:
# Output displays integer representing minimum distance.
# Sample Testcases:
# Input 1
# 16
# 1 5 3 7 2 8 3 4 5 9 9 3 1 3 2 9
# 4 7
# Output 1
# 4
# Input 2
# 16
# 1 5 3 7 2 8 3 4 5 9 9 3 1 3 2 9
# 2 5
# Output 2
# 3



arr = [1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 3, 1, 3, 2, 9]

def num(minvalue, maxvalue):
    nlength = len(arr)
    j = 0
    count = 0
    for i in range(nlength):
        if(j == 0):
            if(arr[i] == minvalue):
                k = 0
                for k in range(i, nlength):
                    if(maxvalue == arr[k]):
                        break
                    else:
                        count = count + 1


            elif(arr[i] == maxvalue):
                    k = 0
                    for k in range(i, nlength):
                        if(minvalue == arr[k]):
                            break
                        else:
                            count = count + 1
                            j = j + 1

    return count


fcase = num(4, 7)
print(fcase)

scase = num(2, 5)
print(scase)



