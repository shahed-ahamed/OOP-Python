class car:

    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.brk = False
        self.clutch = False
        print("Car starting...")

car1 = car()
car1.start()

#unnecessary object ke hide kore shudu dorkari jinish dekhanoi hocche abstraction