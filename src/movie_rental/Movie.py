from src.movie_rental.ChildrenPriceCode import ChildrenPriceCode
from src.movie_rental.NewReleasePriceCode import NewReleasePriceCode
from src.movie_rental.PriceCode import PriceCode
from src.movie_rental.RegularPriceCode import RegularPriceCode


class Movie:
    REGULAR: int = 0
    CHILDRENS: int = 1
    NEW_RELEASE: int = 2

    title: str
    price_code: int

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price_code = price_code

    def get_price_code(self) -> int:
        return self.price_code

    def set_price_code(self, price_code: int):
        self.price_code = price_code

    def get_title(self) -> str:
        return self.title

    def get_price_code_object(self) -> PriceCode:
        match self.price_code:
            case Movie.REGULAR:
                return RegularPriceCode()
            case Movie.NEW_RELEASE:
                return NewReleasePriceCode()
            case Movie.CHILDRENS:
                return ChildrenPriceCode()
