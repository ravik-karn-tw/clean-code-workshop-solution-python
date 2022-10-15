from src.movie_rental.Movie import Movie
from src.movie_rental.Rental import Rental


def test_should_compute_amount_for_documentary():
    rental = Rental(Movie("Movie-1", Movie.DOCUMENTARY), 10)
    assert 40 == rental.amount()
