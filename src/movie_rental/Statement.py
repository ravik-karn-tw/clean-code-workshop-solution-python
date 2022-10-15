class Statement:
    def generate_statement(self, customer_name, rentals):
        return self.__header(customer_name) + self.__body(rentals) + self.__footer(rentals.total_amount(),
                                                                                   rentals.frequent_renter_points())

    def __header(self, customer_name) -> str:
        return "Rental Record for " + customer_name + "\n"

    def __body(self, rentals) -> str:
        return self.__body_formatter(lambda rental: "\t" + rental.get_movie().get_title() + "\t" + \
                                                    str(rental.amount()) + "\n", rentals)

    def __footer(self, total_amount, frequent_renter_points) -> str:
        return "Amount owed is " + str(total_amount) + "\n" + "You earned " + str(
            frequent_renter_points) + \
               " frequent renter points"

    def __body_formatter(self, formatter, rentals) -> str:
        result: str = ""
        for rental in rentals:
            result += formatter(rental)
        return result
