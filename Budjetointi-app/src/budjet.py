class budjet:
    def __init__(self, user):
        self.user = user
        self.total = 0

    def add(self, amount: int):
        self.total += amount

    def substract(self, amount: int):
        self.total -= amount