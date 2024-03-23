
class A:
    def displayA(self):
        print("I am in Class A")

class B(A):   #multi-level inheritance
    def displayB(self):
        print ("I am in Class B")

class C(B):   #multi-level inheritance
    def displayC(self):
        print ("I am in Class C ")

           

obj=C()
obj.displayC()
obj.displayB()
obj.displayA()
