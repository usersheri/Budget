class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __repr__(self):
        return f"{self.date} - {self.category} - ₹{self.amount}: {self.description}"
