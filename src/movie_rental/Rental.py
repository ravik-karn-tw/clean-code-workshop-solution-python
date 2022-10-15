from src.movie_rental.Movie import Movie


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
                this_amount += 2
                if self.get_days_rented() > 2:
                    this_amount += (self.get_days_rented() - 2) * 1.5
            case Movie.NEW_RELEASE:
                this_amount += self.get_days_rented() * 3
            case Movie.CHILDRENS:
                this_amount += 2
                if self.get_days_rented() > 3:
                    this_amount += (self.get_days_rented() - 3) * 1.5
        return this_amount