a=int(input("Enter the value="))
b=int(input("Enter the value="))
try:
    c=a/b
except ZeroDivisionError:
    print("Not allowed")
else:
    print("Value of c=",c)
finally:
    print("End")
