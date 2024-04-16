class school:
    pass  #nothing to pass the step in every condition
s1 = school()  #constructor, creatin object
s2 = school() #s1 ,s2,s3 are refer objects
s3 = school()
print(s1)

# class is a collection of object
# construct the object with help of class
#blueprint model for objects


class school:
    principal = 'johnson'  #class atribut/variable
    def __init__(self,name,age,rollno) :  #special method,initilize
        self.name = name    # s1.name = kumar , object attribute/object variable
        self.age = age   # name,age,rolno,prince are attribute
        self.rolno = rollno
    def change_newage(self, newage):  #instance method 
        self.age = newage
    @classmethod  #decrator
    def change_newpri(cls,new_pri):
        cls.principal = new_pri
    @staticmethod
    def address():  #static method
        print('velachery logi360')
        
       
       

s1 = school("kumar",12,543)  #constructor ,creating object
s2 = school('kannan',13,532)
print(s2.principal)
#school.change_newpri(school,"mani") #without decrator
school.change_newpri("mani") #with decrator
print(s2.principal)
s1.address()  # obj can't able to call static method ,coz no self but using decrator we can call
school.address()




