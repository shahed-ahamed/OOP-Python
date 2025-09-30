class person:
    name="annonymous"
    def change_name(self,name):
        self.name=name
        self.__class__.name= "unknown"
    
p1=person()
p1.change_name("SHAHED")
print(p1.name)
print(person.name)
