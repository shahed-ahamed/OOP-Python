class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

s1 = student("John", 101)
print(s1.name)
print(s1.roll)
del s1.name

print(s1.roll)
  # This will raise an AttributeError since 'name' has been deleted
# AttributeError: 'student' object has no attribute 'name'
  # This will work fine and print 101