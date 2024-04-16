class abc:
    company = "ABC"
    def __init__(self,name,age,rollno) :  #special method,initilize
        self.name = name    # s1.name = kumar , object attribute/object variable
        self.age = age   # name,age,rolno,prince are attribute
        self.rolno = rollno
        
    @classmethod
    def change_names(cls,change_name):
        cls.company +=change_name
    @staticmethod
    def address():
        print('chennai')
s1=abc("mani",23,3223)
abc.change_names(' pvt')
print(s1.company)
s1.address()


    
