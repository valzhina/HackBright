############
# Part 1   #
############
# cl1 = MelonType(name, codem.......)
# cl1.pairings
class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""

        self.pairings = []
        # Fill in the rest
        self.name = name
        self.code = code 
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType("Muskmelon", "musk", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    
    casaba = MelonType("Casaba", "cas", 2003, "orange", False, False) 
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries")
    all_melon_types.append(casaba)

    cren = MelonType("Crenshaw", "cren", 1996, "green", False, False)
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yellow_watermelon = MelonType("Yellow Watermelon", "yw", 2013, "yellow", False, True)
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print("\n")

print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest  {cren: [1993, yellow, true], yw: [2005, green, true]}
    melons_by_code = {}

    for melon in melon_types:
        if melon.code not in melons_by_code:
            melons_by_code[melon.code] = [melon.first_harvest, melon.color, melon.is_seedless]

    return melons_by_code   

      
print(make_melon_type_lookup(make_melon_types()))


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        """ Melons are categorized as sellable or not sellable"""

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    m1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    m2 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    m3 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    m4 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    m5 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    m6 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    m7 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    m8 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    m9 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')

    m = [m1, m2, m3, m4, m5, m6, m7, m8, m9]

    return (m)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
