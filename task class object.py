class employee:
    company_name = "ABC Copmpany"
    def __init__(self,name,empid,role) :
        self.name= name
        self.empid = empid
        self.role = role
    def changeroll(self,newroll):
        self.role= newroll
        
s1 =employee('sam','5454', 'ceo' )
print (s1.company_name)
print(s1.name)
print(s1.empid)
print(s1.role)
s1.changeroll('developer')
print(s1.role)
