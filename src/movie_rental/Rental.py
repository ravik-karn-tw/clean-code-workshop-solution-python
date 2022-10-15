from src.movie_rental.ChildrenPriceCode import ChildrenPriceCode
from src.movie_rental.Movie import Movie
from src.movie_rental.NewReleasePriceCode import NewReleasePriceCode
from src.movie_rental.RegularPriceCode import RegularPriceCode


class Rental:
    movie: Movie
    days_rented: int

    def __init__(self, movie: Movie, days_rented: int):
        self.movie = movie
        self.days_rented = days_rented

    def get_days_rented(self) -> int:
        return self.days_rented

    def get_movie(self) -> Movie:
        return self.movie

    def amount_for(self) -> float:
        this_amount: float = 0
        match self.get_movie().get_price_code():
            case Movie.REGULAR:
                this_amount = RegularPriceCode().amount(self.get_days_rented())
            case Movie.NEW_RELEASE:
                this_amount = NewReleasePriceCode().amount(self.get_days_rented())
            case Movie.CHILDRENS:
                this_amount = ChildrenPriceCode().amount(self.get_days_rented())
        return this_amount
