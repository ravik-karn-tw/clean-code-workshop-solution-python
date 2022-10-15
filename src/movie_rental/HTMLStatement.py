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
