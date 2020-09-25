""" in python there are 4 collection data types 1.list,2.tuple,3.set,4.dictonery
list-list is collection which is mutable(chanageble) and ordered elements .it allows duplicate elements.
     ......................................below there are certain operation................................"""
list=[10,20,30,40,50]
print(list)
list.append(60)
print(list)
list.insert(2,25)
print(list)
list.remove(25)
print(list)
del list[1:3]
print(list)
list.pop()
print(list)
list.pop(1)
print(list)
list.extend([60,70])
print(list)
x=min(list)
print(x)
x=max(list)
print(x)
x=sum(list)
print(x)
list.sort()
print(list)