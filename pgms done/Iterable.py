print('Iterable program\n')
L=['RAM','HANUMAN','SITA','KRISHNA']
mylist=iter(L)
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))

print('\nItearble program using for loop\n')
T=('Rose','Jasmine','Lotus','Lily')
mytuple=iter(T)
for i in range(len(T)):
        print(next(mytuple))

print('\nItearble program to print letter by letter\n')
S="BCA"
myString=iter(S)
print(next(myString))
print(next(myString))
print(next(myString))
555555

print('\nIterators program\n')

class Series(object):
        def __init__(self,low,high):
             self.current=low
             self.high=high
        def __iter__(self):
             return self
        def __next__(self):
             if self.current>=self.high:
                 raise StopIteration
             else:
                 self.current=self.current+1
             return self.current
        
list1=Series(0,10)
print('Series is',list(list1))

