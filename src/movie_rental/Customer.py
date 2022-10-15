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
        result: str = self.__header()
        result += self.__body_formatter(self.__body_line())
        result = self.__footer(result)
        return result

    def __header(self):
        return "Rental Record for " + self.name + "\n"

    def __body_line(self):
        return lambda rental: "\t" + rental.get_movie().get_title() + "\t" + \
                              str(self.__amount_for(rental)) + "\n"

    def __footer(self, result):
        result += "Amount owed is " + str(self.__total_amount()) + "\n"
        result += "You earned " + str(self.__frequent_renter_points()) + \
                  " frequent renter points"
        return result

    def html_statement(self) -> str:
        return self.__html_header() + self.__body_formatter(self.__html_body_line()) + self.__html_footer()

    def __html_header(self):
        return f"<html><h1>Rental Record for <b>{self.name}</b></h1></br>"

    def __html_body_line(self):
        return lambda rental: f" {rental.get_movie().get_title()} {self.__amount_for(rental)}</br>"

    def __html_footer(self):
        return f"Amount owed is <b>{self.__total_amount()}</b></br>" \
               f"You earned <b>{self.__frequent_renter_points()}</b> frequent renter points</html>"

    def __body_formatter(self, formatter) -> str:
        result: str = ""
        for rental in self.rentals:
            result += formatter(rental)
        return result

    def __total_amount(self):
        total_amount: float = 0.0
        for each in self.rentals:
            total_amount += self.__amount_for(each)
        return total_amount

    def __amount_for(self, rental: Rental) -> float:
        this_amount: float = 0
        match rental.get_movie().get_price_code():
            case Movie.REGULAR:
                this_amount += 2
                if rental.get_days_rented() > 2:
                    this_amount += (rental.get_days_rented() - 2) * 1.5
            case Movie.NEW_RELEASE:
                this_amount += rental.get_days_rented() * 3
            case Movie.CHILDRENS:
                this_amount += 2
                if rental.get_days_rented() > 3:
                    this_amount += (rental.get_days_rented() - 3) * 1.5
        return this_amount

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
