class Category:

    def __init__(self, name):
        self.name = name
        self.total: float(2) = 0
        self.ledger = []

    def deposit(self, amount, description="deposit"):
        self.total += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float(2), description="withdrawal"):
        if self.check_funds(amount):
            self.total -= amount
            self.ledger.append({"amount": -amount, "description": description})

    def transfer(self, amount, category, description=""):
        # check if there are funds in account or not, basically if check fund is not False then add
        if self.check_funds(amount) and self.total >= amount:
            self.withdraw(amount, description=f"Transfer to {category.name}")
            category.deposit(amount, description=f"Transfer to {self.name}")
            return True
        return self.check_funds(amount), f"please add INR {amount - self.total} to the account"

    def get_balance(self):
        return self.total

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False, "Insufficient funds"
        return True

    def __repr__(self):
        line1 = f"""{self.name.center(30, '*')} \n"""

        line_items = [(self.ledger[i]["description"][:23] + str(self.ledger[i]["amount"])[:7].
                       rjust(30 - len(self.ledger[i]["description"]))) for i in range(len(self.ledger))]
        string_items = "\n".join(line_items) + "\n"
        total_amount = "Total:  " + str(self.get_balance())
        return f"{line1}{string_items}{total_amount}"


food = Category('Food')
clothing = Category('Clothing')

food.transfer(50.75, clothing)
food.deposit(500)
food.transfer(25.85, clothing)
food.withdraw(56)
clothing.transfer(97.22, food)
food.ledger
clothing.ledger
