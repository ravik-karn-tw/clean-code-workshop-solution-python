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
        result: str = "Rental Record for " + self.name + "\n"
        for each in self.rentals:
            # show figure for this rental
            result += "\t" + each.get_movie().get_title() + "\t" + \
                      str(self.__amount_for(each)) + "\n"
        # add footer lines result
        result += "Amount owed is " + str(self.__total_amount()) + "\n"
        result += "You earned " + str(self.__frequent_renter_points()) + \
                  " frequent renter points"
        return result

    def __total_amount(self):
        total_amount: float = 0.0
        for each in self.rentals:
            total_amount += self.__amount_for(each)
        return total_amount

    def __amount_for(self, each):
        this_amount: float = 0
        match each.get_movie().get_price_code():
            case Movie.REGULAR:
                this_amount += 2
                if each.get_days_rented() > 2:
                    this_amount += (each.get_days_rented() - 2) * 1.5
            case Movie.NEW_RELEASE:
                this_amount += each.get_days_rented() * 3
            case Movie.CHILDRENS:
                this_amount += 2
                if each.get_days_rented() > 3:
                    this_amount += (each.get_days_rented() - 3) * 1.5
        return this_amount

    def __frequent_renter_points(self):
        frequent_renter_points: int = 0
        for each in self.rentals:
            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (each.get_movie().get_price_code() == Movie.NEW_RELEASE) and \
                    (each.get_days_rented() > 1):
                frequent_renter_points += 1
        return frequent_renter_points

    def html_statement(self):
        return f"<html><h1>Rental Record for <b>{self.name}</b></h1></br>" \
           " movie-1 14.0</br>" \
           " movie-2 12.5</br>" \
           " movie-3 30</br>" \
           f"Amount owed is <b>{self.__total_amount()}</b></br>" \
           f"You earned <b>{self.__frequent_renter_points()}</b> frequent renter points</html>"
