class car:
    x="BMW"
    def __init__(self,x):
        self.x=x
    def model(self):
        print(self.x)
       

class type:
    x="benz"
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def model(self):
        print(self.x,self.y)   
obj=type("model","year")
obj1=car("model")
obj.model()
obj1.model()

        


        