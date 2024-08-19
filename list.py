x=['apple','orange','grape','watermelon','anar','avacado']
print(x)
print(type(x))
print(len(x))
print(x[1])
print(x[1:3])
print(x[1:])
print(x[: 2])
print(x[-2])
print(x[-3:-1])
print("orange" in x)
print("grape " not in x)
for i in x:
    print(i)
x[1]= "banana"
print(x)
x.append("mango") 
print(x) 
x.insert(2,"anar") 
print(x)
y=[1,2,3,4,5]
x.extend(y)
print(x)
x.remove("apple")
print(x)
x.pop(2)
print(x)
x.pop()
print(x)
del x[2]
print(x)
x.clear()
print(x)
#del x
z=["india","portugal","brazil","france"]
print(z)
z.sort()
print(z)
z.sort(reverse=True)
print(z)
a=z.copy()
print(a)
b=list(a)
print(b)
print(z+a)
print(z.count("india"))
z.copy()
print(z)



