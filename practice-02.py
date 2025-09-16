class Account:
    def __init__(self,bal , acc):
        self.bal = bal
        self.acc = acc

    #debit method
    def debit(self, amount):
        self.bal -= amount
        print("Debited:", amount)
        print("Remaining balance:", self.bal)

    #credit method
    def credit(self, amount):
        self.bal += amount
        print("Credited:", amount)
        print("New balance:", self.bal)

    def get_balance(self):
        return self.bal

acc1 = Account(5000, "12345")
acc1.debit(1000)
acc1.credit(15466)
acc1.debit(23454365454)
print("Current Balance:", acc1.get_balance())      