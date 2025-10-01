class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def sum(self):
        print(f"{self.real} + {self.img}i")
        
    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)
    
    def __sub__(self, num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newreal, newimg)
        
        
num1 = Complex(2, 3)
num2 = Complex(4, 5)
num1.sum()
num2.sum()
num3 = num1 + num2
num3.sum()
num4 = num1 - num2
num4.sum()
