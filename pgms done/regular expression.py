import re
print("------menu-------")
print("1.Use of ^ caret")
print("1.Use of $ dollar")
print("1.Use of [] range")
print("1.Use of * asterisk")
print("1.Use of \ backslash")
print("6.Exit")
while(True):
    i=int(input("Enter your choice:"))
if(i==1):
    s=input("Enter a String:")
    x=re.findal("^python",s)
if x:
    print("yes, the string-",s,":starts with python")
else:
    print("No, the string-",s,"doesnt sart with The")
      
            
      
