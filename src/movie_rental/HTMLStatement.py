class HTMLStatement:
    def generate_html_statement(self, customer_name, rentals, total_amount, frequent_renter_points):
        return self.__html_header(customer_name) + self.__html_body(rentals) + self.__html_footer(total_amount,
                                                                                                  frequent_renter_points)

    def __html_header(self, customer_name) -> str:
        return f"<html><h1>Rental Record for <b>{customer_name}</b></h1></br>"

    def __html_body(self, rentals) -> str:
        return self.__body_formatter(
            lambda rental: f" {rental.get_movie().get_title()} {rental.amount_for()}</br>", rentals)

    def __body_formatter(self, formatter, rentals) -> str:
        result: str = ""
        for rental in rentals:
            result += formatter(rental)
        return result

    def __html_footer(self, total_amount, frequent_renter_points) -> str:
        return f"Amount owed is <b>{total_amount}</b></br>" \
               f"You earned <b>{frequent_renter_points}</b> frequent renter points</html>"
