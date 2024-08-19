x = int(input("Enter a number: "))    
f = 1    
if x < 0:    
   print(" Factorial does not exist ")    
elif x == 0:    
   print("The factorial  is 1")    
else:    
   for i in range(1,x + 1):    
       f = f*i    
   print("The factorial of",x,"is",f)   