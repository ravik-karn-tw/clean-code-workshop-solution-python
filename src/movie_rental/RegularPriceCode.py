class RegularPriceCode:
    def amount(self, days_rented):
        this_amount: float = 2
        if days_rented > 2:
            this_amount += (days_rented - 2) * 1.5
        return this_amount
