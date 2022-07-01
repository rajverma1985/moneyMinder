class Accounts:
    acc_groups = ['cash', 'upi', 'credit card', 'debit card', 'savings']

    def __init__(self, name: str, group: str, notes: str = None, amount: int = None):
        self.group = group
        self.name = name
        self.amount = amount
        self.notes = notes
