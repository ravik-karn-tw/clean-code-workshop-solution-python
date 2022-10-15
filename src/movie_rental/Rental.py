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
        return self.get_movie().get_price_code_object().amount(self.days_rented)
