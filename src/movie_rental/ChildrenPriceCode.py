class ChildrenPriceCode:
    def amount(self, days_rented):
        this_amount = 2
        if days_rented > 3:
            this_amount += (days_rented - 3) * 1.5
        return this_amount
