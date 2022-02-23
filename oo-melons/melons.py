
"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty):
        """ """

        self.species = species
        self.qty = qty
        self.shipped = False
       
        
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas melon":
            base_price = base_price * 1,5

        total = (1 + self.tax) * self.qty * base_price
        return total
    

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

  
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type= "international"
    tax = 0.17
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code



    def get_country_code(self):
        """Return the country code."""

        return self.country_code

# """Classes for melon orders."""

# class AbstractMelonOrder:
#     """An abstract base class that other Melon Orders inherit from."""
#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
    
#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         if self.species == 'Christmas':
#             base_price *= 1.5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class DomesticMelonOrder(AbstractMelonOrder):
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes."""
#         AbstractMelonOrder.__init__(self, species, qty) # can use super()
#         self.order_type = "domestic"
#         self.tax = 0.08




# class InternationalMelonOrder(AbstractMelonOrder):
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes."""
#         super().__init__(species, qty)
#         self.country_code = country_code
#         self.order_type = "international"
#         self.tax = 0.17
    
#     def get_total(self):
#         """Calculate price, including tax."""

#         if self.qty < 10:
#             flat_fee = 3
        
#         total = super().get_total() + flat_fee

#         return total

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code

# class GovernmentMelonOrder(AbstractMelonOrder):
#     """An government melon order."""

#     def __init__(self, species, qty):
#         super().__init__(species, qty)
#         self.passed_inspection = False
#         self.order_type = "government"
#         self.tax = 0
    
#     def mark_inspection(self, passed):
#         """updates whether or not the melon has passed"""

#         self.passed_inspection = passed
