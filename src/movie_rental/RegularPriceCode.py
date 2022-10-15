class RegularPriceCode:
    def amount(self, days_rented):
        amount: float = 2
        if days_rented > 2:
            amount += (days_rented - 2) * 1.5
        return amount
