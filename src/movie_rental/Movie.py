from src.movie_rental.ChildrenPriceCode import ChildrenPriceCode
from src.movie_rental.DocumentaryPriceCode import DocumentaryPriceCode
from src.movie_rental.NewReleasePriceCode import NewReleasePriceCode
from src.movie_rental.PriceCode import PriceCode
from src.movie_rental.RegularPriceCode import RegularPriceCode


class Movie:
    REGULAR: int = 0
    CHILDRENS: int = 1
    NEW_RELEASE: int = 2
    DOCUMENTARY: int = 3

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

    def __get_price_code_object(self) -> PriceCode:
        match self.price_code:
            case Movie.REGULAR:
                return RegularPriceCode()
            case Movie.NEW_RELEASE:
                return NewReleasePriceCode()
            case Movie.CHILDRENS:
                return ChildrenPriceCode()
            case Movie.DOCUMENTARY:
                return DocumentaryPriceCode()

    def amount(self, days_rented):
        return self.__get_price_code_object().amount(days_rented)
