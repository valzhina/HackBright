"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def __repr__(self):
        return(f"Customer: {self.first_name} {self.last_name}")


def read_customers_from_file(filepath):
    """Read customers data and populate dictionary of customers.

    Dictionary will be {email: customer object}
    """
    customers ={}

    with open(filepath) as file:
        for line in file:
            first_name, last_name, email, password = line.rstrip().split("|")
            customers[email] = Customer(first_name, last_name, email, password)
    
    return(customers)


def get_by_email(email):
    return(cust_data.get(email,False)) 

cust_data = read_customers_from_file('customers.txt')
