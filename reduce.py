#reduce: used to perform operation on list
# to perform add operaton on list:::

import functools
lst=[1,2,3,4,5]
addition=functools.reduce(lambda a,b:a+b,lst)
print(addition)