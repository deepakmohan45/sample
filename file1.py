x=open("file1.txt","w")
print(x.write("my favuorite batter is rohith sharma"))
x=open("file1.txt","r")

y=x.read()
x.close()

x=open("file2.txt","w")
print(x.write(y))
x.close()