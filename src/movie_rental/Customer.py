from src.movie_rental.HTMLStatement import HTMLStatement
from src.movie_rental.Statement import Statement
from src.movie_rental.Movie import Movie
from src.movie_rental.Rental import Rental


class Customer:
    name: str
    rentals: list[Rental]

    def __init__(self, name: str):
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def get_name(self) -> str:
        return self.name

    def statement(self) -> str:
        return Statement().generate_statement(self.name, self.rentals, self.__total_amount(),
                                              self.__frequent_renter_points())

    def html_statement(self) -> str:
        return HTMLStatement().generate(self.name, self.rentals, self.__total_amount(),
                                        self.__frequent_renter_points())

    def __total_amount(self) -> float:
        total_amount: float = 0.0
        for each in self.rentals:
            total_amount += each.amount_for()
        return total_amount

    def __frequent_renter_points(self) -> float:
        frequent_renter_points: int = 0
        for each in self.rentals:
            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (each.get_movie().get_price_code() == Movie.NEW_RELEASE) and \
                    (each.get_days_rented() > 1):
                frequent_renter_points += 1
        return frequent_renter_points
