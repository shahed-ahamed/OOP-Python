class student:
    college = "DIU"

    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("This is constructor")
       
    def display(self):
        print(f"Name: {self.name}, ID: {self.id}, College: {student.college}")

    def getmark(self, mark):
        self.mark = mark
        return self.mark


s1 = student("Shahed", 101)
print(s1.name)
s1.display()
s1.getmark(95)
print(s1.mark)
s2 = student("Rony", 102)
print(s2.name)
s2.display()
s2.getmark(88)
print(s2.mark)