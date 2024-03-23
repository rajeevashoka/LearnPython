class A:
    def displayA(self):
        print("I am in Class A")

class B: 
    def displayB(self):
        print ("I am in Class B")

class C(A,B):   #multiple -inheritance   python support only
    def displayC(self):
        print ("I am in Class C ")


           

obj=C()
obj.displayC()
obj.displayB()
obj.displayA()
