x={"name":"Deepak","age":25,"place":"kollam"}
print(x)
print(type(x))
print(len(x))
print(x["name"])
print(x.get("name"))
print(x.keys())
print(x.values())
print(x.items())
print("name" in x)
print("name" not in x)
x["place"]="sasthankottah"
print(x)
x.update({"age":26})
print(x)
x["hobby"]="Cricket"
print(x)
x.update({"favrtbatter":"Rohit sharma"})
print(x)
for i in x:
    print(i)
for i in x:
    print(x[i])  
for i in x.keys():
    print(i)  
for i in x.items():
    print(i)      
for i in x.values():
    print(i)
y=x.copy()  
print(y) 
z=dict(x)   
print(z) 
x.pop("name") 
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
x.clear()
print(x)
#del x
#print(x)
family={"child1":{"name":"deepak","age":25},"child2":{"name":"devika","age":28},"child3":{"name":"aravind","age":29}}
print(family)
print(family["child2"])
print(family["child2"]["age"])