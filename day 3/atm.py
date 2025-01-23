class ATM:
    def __init__(self,pin,balance=0):
        self.pin = pin
        self.balance = balance

    def withdraw(self):
        enter_pin = int(input("Enter a pin: "))
        if self.pin == enter_pin:
            enter_amount = int(input("Enter a amount to be withdraw: "))
            if enter_amount >= self.balance:
                return "Insufficient balance."
            elif enter_amount <=0:
                return "Invalid amount"
            else:
                self.balance -= enter_amount
                return f"Withdraw successfully. New balance is: {self.balance}"

    def checkbalance(self):
        enter_pin = int(input("Enter a pin: "))
        if self.pin == enter_pin:
            return f"Your account balance is {self.balance}"

atm = ATM(pin=1234,balance=10000)

# print(atm.withdraw())
print(atm.checkbalance())


