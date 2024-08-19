# for i in range(1,6,2):
#     if i==3:
#         break  
#     print(i) 

#     a=[1,2,3,4,5]   
# b=["a","b","c","d","e"] 
# for i in a:
#     for j in b:
#         print(i,j) 



x=lambda a,b: a+b
print(x(45,10))
x=["ind","pak","aus"]
y=list(map(lambda a :str.upper(a) , x))
print(y)