def fact(n):
    if n==1:
        return n
    else:
        return n* fact(n-1)

num=int(input("enter the number"))
if num <0:
    print("factorial not exist")
elif num==0:
    print("factorial of 0 is 1")   
else:
    print("factorial of number is",fact(num))     
