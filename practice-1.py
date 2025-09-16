class student:

    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
    
    def get_avg(self):
        return sum(self.marks) / len(self.marks)
    
s1 = student("Shahed", [95, 89, 76])
print(s1.get_avg())