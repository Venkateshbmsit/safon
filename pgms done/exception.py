try:
    print("try block")
    x=int(input('Enter a number:'))
    y=int(input('Enter another number:'))
    if y>x:
        z=y/x
        raise TypeError
    else:
        z=x/y
except TypeError:
    print("except TypeError block")
    print("Invalid operation")
except ValueError:
    print("except ValueError block")
    print("Invalid literal for int() with base 10")
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("In else block Division is=",z)
finally:
    print("finally block")
