# x=open("filecontent1.txt","x")
# y=open("filecontent2.txt","x")
# z=open("filecontent3.txt","x")

x=open("filecontent1.txt","w")
print(x.write("india is my country"))
x=open("filecontent1.txt","r")
a=x.read()
x.close()

y=open("filecontent2.txt","w")
print(y.write("i am from kerala"))
y=open("filecontent2.txt","r")
b=y.read()

y.close()

z=open("filecontent3.txt","w")

z.write(a)
y=open("filecontent2.txt","a")
z.write(b)


z.close()