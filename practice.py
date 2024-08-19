x="deepak mohan"
print(x)
print(type(x))
print(len(x))
print("deepak" in x)
print("deepak" not in x)
#slicing

print(x[2:5])
print(x[:5])
print(x[2:])
print(x[-5 :-2])

#modifying

print(x.upper())
print(x.lower())
y="   rohith  sharma "
print(y)
print(y.strip())
print(y.replace("o","m"))
print(y)
print(y.split(","))
z=x+y
print(z)
print(y.count("e"))

#fstring

age=35
txt=f"my name is deepak, i am {age}"
print(txt)