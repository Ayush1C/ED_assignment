# Type Casting = Where we can convert one data type into another data type.
# int()
# float()
# str()
# bool()
# complex()
# list()
# set()
# tuple()
# dict()

#num=10
#name = ayush

#print(num)
#print("int to float :",float(name))
#print("int to str :",str(num))
#print("int to bool :",bool(num))
#print("int to complex :",complex(num))

from os import lstat


lst = [10,2,6,3,1,5,6,7,8,8,6]
print(lst)

unique = set(lst)
print(unique,"----->",type(unique))

lst1 = list(unique)
print(lst1,"--->",type(lst1))

unmod = tuple(lst1)
print(unmod,"---->",type(unmod))