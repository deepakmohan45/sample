try:
    print(x)
except:
    print("check the code")


try:
    print(x)
except NameError: 
    print("variable is not defined")   
except:
    print("check the code")  


try:
    print("name") 
except:
    print("check")
else:
    print("name") 
finally:
    print("successfully executed")   

x=-5
if x <0:
    raise Exception(" negative numbers are not allowed")               