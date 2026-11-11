class BankAccount:
    
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. Balance: ₹{self.__balance}")
        
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Balance: ₹{self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Alice", 5000)

acc.deposit(2000)

acc.withdraw(1500)

print("Final Balance:", acc.get_balance())

print("prn no. 26013010907")
print("name: Shreyansh Singh")
