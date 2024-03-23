class Student:
    def __init__(self) -> None:
        self.__name=""    #private variable
    def getname(self):
        return self.__name   
    def setName(self,Name):
        self.__name=Name

obj=Student()
obj.setName("Rajeev")
print (obj.getname())