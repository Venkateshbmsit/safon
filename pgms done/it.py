print('iterable program')
L=['MANGO','APPLE','ORRANGE']
mylist=iter(L)
print(next(mylist))
print(next(mylist))
print(next(mylist))
print('\niterable program using for loop')
T=['ROSE','LILLY','LOTUS']
mytuple=iter(L)
for i in range(len(T)):
    print(next(mytuple))
    print('\niterable program to print letter by letter')
    S='BCA'
    mystring=iter(S)
    print(next(mystring))
    print(next(mystring))
    print(next(mystring)
