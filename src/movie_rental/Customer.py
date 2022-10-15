from src.movie_rental.HTMLStatement import HTMLStatement
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
        return self.__header() + self.__body() + self.__footer()

    def __header(self) -> str:
        return "Rental Record for " + self.name + "\n"

    def __body(self) -> str:
        return self.__body_formatter(lambda rental: "\t" + rental.get_movie().get_title() + "\t" + \
                                                    str(rental.amount_for()) + "\n")

    def __footer(self) -> str:
        return "Amount owed is " + str(self.__total_amount()) + "\n" + "You earned " + str(
            self.__frequent_renter_points()) + \
               " frequent renter points"

    def html_statement(self) -> str:
        return HTMLStatement().generate(self.name, self.rentals, self.__total_amount(),
                                        self.__frequent_renter_points())

    def __body_formatter(self, formatter) -> str:
        result: str = ""
        for rental in self.rentals:
            result += formatter(rental)
        return result

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
