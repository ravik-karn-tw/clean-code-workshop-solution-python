class ChildrenPriceCode:
    def amount(self, days_rented):
        amount = 2
        if days_rented > 3:
            amount += (days_rented - 3) * 1.5
        return amount
