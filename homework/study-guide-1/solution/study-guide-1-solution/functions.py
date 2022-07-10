"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""


# SOLUTIONS!

###############################################################################

# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".


def hello_world():
    """Prints hello world."""

    print("Hello World")


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.


def say_hi(name):
    """Greet a user by name."""

    print(f"Hi {name}")


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.


def print_product(a, b):
    """Print product of two integers."""

    print(a * b)


# 4. Write a function that takes a string and an integer and
#    prints the string that many times


def repeat_string(message, times_to_repeat):
    """Print the messages as many times as given."""

    # Neat! Python can multiply a string by an integer!

    print(message * times_to_repeat)


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".


def print_sign(num):
    """For num, print if it's higher/lower/equal to zero."""

    if num > 0:
        print("Higher than 0")
    elif num < 0:
        print("Lower than 0")
    else:
        print("Zero")


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


def is_divisible_by_three(num):
    """Is this number divisible by 3?"""

    # We'll use the "modulus operator", which returns the
    # remainder of division.

    return num % 3 == 0


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.


def num_spaces(sentence):
    """Return the number of spaces in the sentence."""

    spaces = 0

    for char in sentence:
        if char == " ":
            spaces += 1  # same as spaces = spaces + 1
    return spaces


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.


def total_meal_price(meal_price, tip=0.15):
    """Find the total price of a meal.

    The total price is the meal price plus the tip.
    """

    return meal_price + (meal_price * tip)


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two
#    strings should be returned in a list.


def sign_and_parity(num):
    """Return a list of [sign, parity]"""

    if num >= 0:
        sign = "Positive"
    else:
        sign = "Negative"

    if num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    return [sign, parity]


# Then, write code that shows the calling of this function
# on a number and unpack what is returned into two
# variables --- sign and parity (whether it's even or odd).
# Print sign and parity.

my_sign, my_parity = sign_and_parity(7)

print(my_sign)
print(my_parity)


###############################################################################

# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name.


def full_title(name, title="Engineer"):
    """Return the full  for a person."""

    return f"{title} {name}"


# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.


def write_letter(name, title, sender):
    """Print filled in form letter"""

    receiver = full_title(name, title)

    print(f"Dear {receiver}, I think you are amazing! Sincerely, {sender}")


###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print
