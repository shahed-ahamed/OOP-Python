class student:
    def __init__(self,phy,chem,math):
        self.phy= phy
        self.chem= chem
        self.math= math
        self.avarage=str((self.phy+self.chem+self.math)/3)+"%"
        
s1= student(80,90,70)
s2= student(85,95,75)
print(s1.avarage)
print(s2.avarage)
