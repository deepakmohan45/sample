class india:
    x="kerala"
obj= india()
print(obj.x)


class kerala:
     def __init__(self,x,y) :
          self.x=x
          self.y=y
     def district(self):
          print(self.x,self.y)
obj=kerala("kollam","alapuzha")  
obj.district()   


class animal:
     def __init__(self,x) :
          self.x=x
     def dog(self):
          print(self.x)

class cat(animal):
     pass
obj=cat("colour")
obj.dog()
          
          
          
          