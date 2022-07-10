log_file = open("um-server-01.txt") # opens a text file and returns the contents of the file as python objects


def sales_reports(log_file): # creates a function 
    for line in log_file: # creates a loop to go through a file line by line
        line = line.rstrip() # removes whitespace at the front and the back of the string
        day = line[0:3] # creates a new string with 3 first letters
        if day == "Mon": # compares a new string to a day of the week
            print(line) # prints entire line


sales_reports(log_file) # calls function and passing into a function the parameters from original text file
