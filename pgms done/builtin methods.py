print('--------------------Built-in methods of string---------------------')
str='welcome to python'
print('Right')
a=str.rjust(50,'#')
print(a)
print('Left')
b=str.ljust(50,'#')
print(b)
print('center')
c=str.center(50,'#')
print(c)
print('\nLeft strip')
d=c.lstrip('#')
print(d)
print('\nRight strip')
e=c.rstrip('#')
print(e)
print('\nstrip')
f=c.strip('#')
print(f)
print('\nCounting the char')
h=input('Enter the char:')
g=str.count(h)
print(g)
print('\n-------------------Built-in methods of list----------------------')
li1=[1,2,3,4,5,]
li2=[4,5,6,7,8]
print('Length of first list:')
print(len(li1))
print('Length of second list:')
print(len(li2))
print('Max element of first list:')
print(max(li1))

print('Min element of first list:')
print(min(li1))

print('Appending element')
li1.append(8)
print(li1)
print('Extending list:')
seq=['a','b','c','d']
li1.extend(seq)
print(li1)



