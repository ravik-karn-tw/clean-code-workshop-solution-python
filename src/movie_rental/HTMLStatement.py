def html_header(customer_name) -> str:
    return f"<html><h1>Rental Record for <b>{customer_name}</b></h1></br>"


def html_body(rentals) -> str:
    return __body_formatter(
        lambda rental: f" {rental.get_movie().get_title()} {rental.amount_for()}</br>", rentals)


def __body_formatter(formatter, rentals) -> str:
    result: str = ""
    for rental in rentals:
        result += formatter(rental)
    return result


def html_footer(total_amount, frequent_renter_points) -> str:
    return f"Amount owed is <b>{total_amount}</b></br>" \
           f"You earned <b>{frequent_renter_points}</b> frequent renter points</html>"


def generate_html_statement(customer_name, rentals, total_amount, frequent_renter_points):
    return html_header(customer_name) + html_body(rentals) + html_footer(total_amount,
                                                                         frequent_renter_points)