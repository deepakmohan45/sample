x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))

if x>=y and x>=z:
    print(x," is largest number")
elif y>=x and y>=z:
    print(y," is largest number")   
else:
    print(z," is largest number")     