from src.movie_rental.Movie import Movie
from src.movie_rental.Rental import Rental


class Rentals(list[Rental]):
    def total_amount(self) -> float:
        total_amount: float = 0.0
        for each in self:
            total_amount += each.amount_for()
        return total_amount

    def frequent_renter_points(self) -> float:
        frequent_renter_points: int = 0
        for each in self:
            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (each.get_movie().get_price_code() == Movie.NEW_RELEASE) and \
                    (each.get_days_rented() > 1):
                frequent_renter_points += 1
        return frequent_renter_points
