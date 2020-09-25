"""" dict-dict is unordered,mutable collection.
          2)in dict we use keys and values"""
#creation
thisdict={1:'rohit',2:'vinayak',3:'ghadage'}
print(thisdict)
#get
x=thisdict.get(1)
print(x)
#adding
thisdict[4]="vikram"
print(thisdict)
#change
thisdict[3]="tanaji"
print(thisdict)
#pop
thisdict.pop(4)
print(thisdict)
#popitem
thisdict.popitem()
print(thisdict)
#delete
del thisdict[1]
print(thisdict)
#copy
newdict=thisdict.copy()
print(newdict)