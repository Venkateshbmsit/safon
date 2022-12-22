import re
print("--------MENU-------")
print("1.Use of^caret")
print("2.Use of$dollar")
print("3.Use of[]range")
print("4.Use of*asterisk")
print("5.Use of\ backslash")
print("6.Exit")
while(True):
    i=int(input("Enter your choice:"))
    if(i==1):
        s=input("Enter a String:")
        x=re.findall("^python",s)
        if x:
            print("Yes,the string-",s,":starts with python")
        else:
            print("No,the string-",s,"doesnt start with the")
        break;
    elif i==2:
        s=input("Enter a String:")
        x=re.findall("python$",s)
        if(x):
            print("Yes,the string-",s,"ends with python")
        else:
            print("No,the string-",s,"doesnt end with python")
        break;
    elif(i==3):
        s=input("enter a String:")
        x=re.findall("[a-m]",s)
        print(x)
        break;
    elif(i==4):
        s=input("Enter a String:")
        x=re.findall("ai*",s)
        print(x)
        break;
    elif(i==5):
        s=input("Enter a String:")
        x=re.findall("\n",s)
        print(x)
        break;
    else:
        print("Inavlid Choice")
