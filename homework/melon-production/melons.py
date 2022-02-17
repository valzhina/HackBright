import robots


class Melon:
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return f"{self.color} {self.weight:.2f} lbs {self.melon_type}"


# Class Squash inherits from class Melon and in addition in prep method it paints the given melon to green.

class Squash(Melon):
    """Winter squash"""

    def prep(self):

        super().prep()
        robots.painterbot.paint(self)

cl1 = Squash('squash 23')
cl1.prep()
print(cl1.melon_type)