#function overloading --> same function works with disfferent args , return according to arg provided  

class WS:
    def dispalyInfo(self,name=''):
        print ("Welcome to Patna "+name)

obj=WS()
obj.dispalyInfo()
obj.dispalyInfo("Rajeev")

print ('----------------------------------------------')


class WP:
    def dispalyInfo(self):
        print ("Welcome to Patna ")
class WN(WP):
    def dispalyInfo(self):
        print("Elcome to Nalanda")   #function overriden here   #saves memory
        super().dispalyInfo()        # avoiding function overriding
    
obj=WN()
obj.dispalyInfo()