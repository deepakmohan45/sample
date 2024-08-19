# def my_fun():
#     print("deepak")
# my_fun() 

def my_fun(a,b):
    print(a+b)
my_fun(5,6)    


def my_fun(*a):
    print(a[2]+a[3])
my_fun(2,3,4,5,)


def my_fun(x,y,z):
    print(x+y+z)
my_fun(x=3,z=5,y=6) 

def my_fun(**a):
    print(a["x"]+a["y"])
my_fun(x=3,y=5,z=7)    


def my_fun(a=3,b=4):
    print(a+b)
my_fun(5,6)  
my_fun()  


def my_fun(a):
    return a + 10
print("the output is",my_fun(5))

def my_fun(a):
    pass


x=("india","pak","srilanka")
def my_fun(a):
    print(a[1:2])
my_fun(x)  

def my_fun(b):
    for i in b:
        print(i)
my_fun(x)        


x=lambda a : a+10
print(x(5))

x=lambda a,b: a+b
print(x(45,10))
x=["ind","pak","aus"]
y=list(map(lambda a :str.upper(a) , x))
print(y)

x=[3,4,5,6]
y=list(filter(lambda a : a>5,x))
print(y)