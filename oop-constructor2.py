#constructor is self called while creating object only

class Democalss:
    a=10
    def __init__(self) -> None:
        print("I am self called")
    def showval(self):
        print (self.a)
        b=20+self.a
        self.c=30+b   #new variable cab be defined using self.variable
        print (b,self.c)
    def showval1(self,a,b):
        print (a+b)



obj=Democalss()
print (obj.a)
obj.showval()

obj.showval1(40,50)