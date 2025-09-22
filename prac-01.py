class person:
    __name="anynomous"
    
    def __hello(self,name):
        print("hello")
        
    def welcome(self):
        self.__hello(self.__name)
        
p1=person()
print(p1.welcome())   # Output: hello, then None
   