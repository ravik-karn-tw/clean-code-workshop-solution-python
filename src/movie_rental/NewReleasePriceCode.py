from src.movie_rental.PriceCode import PriceCode


class NewReleasePriceCode(PriceCode):
    def amount(self, days_rented):
        return days_rented * 3
