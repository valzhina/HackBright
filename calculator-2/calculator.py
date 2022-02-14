"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# we use "tokenizing" to turn "+ 1 2" into a list [+, 1, 2] for the functions in arithmetic to use. 

# input_problem = input()

# tokens = input_problem.split(' ')cd

while True:
    input_problem = input("Give us an operator and two numbers ")

    tokens = input_problem.split(' ')

   # print(tokens)
    # print(tokens[0])
    if tokens[0] not in ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']:
        print("Oops! That's not a valid operator!")  
    else:
        try:
            if tokens[0] in ['square', 'cube']:
                num1 = int(tokens[1])
            else:   
                num1 = int(tokens[1])
                num2 = int(tokens[2])
            if tokens[0] == "+":
                print(add(int(tokens[1]), int(tokens[2])))

            elif tokens[0] == "-":
                print(subtract(int(tokens[1]), int(tokens[2])))

            elif tokens[0] == "*":
                print(multiply(int(tokens[1]), int(tokens[2])))

            elif tokens[0] == "/":
                print(divide(int(tokens[1]), int(tokens[2])))

            elif tokens[0] == "square":
                print(square(int(tokens[1])))

            elif tokens[0] == "cube":
                print(cube(int(tokens[1])))

            elif tokens[0] == "pow":
                print(pow(int(tokens[1]), int(tokens[2])))

            elif tokens[0] == "mod":
                print(mod(int(tokens[1]), int(tokens[2])))

        except ValueError:  
            print("Oops! That's not a valid number!") 
        