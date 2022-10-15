from src.movie_rental.HTMLStatement import HTMLStatement
from src.movie_rental.Rentals import Rentals
from src.movie_rental.Statement import Statement
from src.movie_rental.Rental import Rental


class Customer:
    name: str
    rentals: Rentals

    def __init__(self, name: str):
        self.name = name
        self.rentals = Rentals()

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def get_name(self) -> str:
        return self.name

    def statement(self) -> str:
        return Statement().generate_statement(self.name, self.rentals)

    def html_statement(self) -> str:
        return HTMLStatement().generate(self.name, self.rentals)
