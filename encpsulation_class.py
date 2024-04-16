class parent:
    company = "public company"
    _company = "protect company"
    __company = "private company"
    def __init__(self,name,_name,__name) :
        self.name=name
        self._name = _name
        self.__name = __name
    def show(self):
        print(self.company)
        print(self._company)
        print(self.__company)  #accessible
class child(parent):
    def __init__(self):
        pass
    def show(self):
        print(self.company)
        print(self._company)
        print(self.__company) #can't access as its private
        
p1= parent('ganesh','kala','sam')
print(p1._company)   # ethically should not access it is protected
#print(p1.__company)  # not accessible as it private  
c1 = child()
c1.show()
p1.show()

