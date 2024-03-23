#making method and variable private , private var and methods can called inside class only. Cannot called from obj

class Student:
    __name="Ravi"   #private var 
    def __init__(self) -> None:
        print(self.__name)  #private method calling in constructor
        self.__displayInfo()
    def __displayInfo(self):   #private method
        print ("Wlecome to Patna")

obj=Student()
