class A:
    varA = "welcome to A"
    
class B: 
    varB = "welcome to B"
    
class C(A, B):
    varC = "welcome to C"
    
c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

#ekhane C class A and B class ke inherit korse tai C class er object diye A and B class er variable access kora jacche.
