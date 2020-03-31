from itertools import islice
import time

print("Lets split a file today!")
print("Make sure that I'm in the same directory as the file you want to split!")
print("You are running the JSON version of big-data-splitter\n")

################# VARIABLES TO CHANGE #################

# File to split (This is going to be your HUGE json file)
file_to_split = input("What file are we splitting today? (Please add the file extension): ")

# This is going to be the "base" file name for all your new files. Make it meaningful!
filename = input("What's the base name of our new files? ")

# This is how many files you want
desired_file_number = int(input("How many new files would you like to create in total? "))

# This is how many lines you want
number_of_lines = int(input("How many lines do you want each file to be of the file_to_split? "))

#######################################################

print("Hang tight, I'll get started")

################# Below is the magic #################

extension = ".json"


# Creates a function that will automatically concatenates inputs as a single string
def file_name(file_number, file, number_of_lines, extension):
    filenumber_string = str(file_number)
    file_string = str(file)
    number_of_lines_string = str(number_of_lines)
    extension = str(extension)

    return filenumber_string + "_" + file_string + "_" + number_of_lines_string + extension


# Initialize blank list for appending
result = []
# automatic file_name variables
file_number = 1
# Initializes line variables
start = 0
end = start + number_of_lines

# Open's the file as inputfile
with open(file_to_split) as inputfile:
    """
    This will start a loop that will read start # of lines until end # of lines
    Then it will save that file with a useful name (based off variables)
    Then it will loop back until the amount of file_numbers is <= desired_file_number
    """
    # starts logical loop for checking the file_number
    while file_number <= desired_file_number:
        for line in islice(inputfile, start, end):
            result.append(line)
        #  Creates a new file of the selected set.
        with open(file_name(file_number, filename, number_of_lines, extension), 'w') as new_file:
            for line in result:
                new_file.write("%s" % line)

        print(f"File {file_number} complete...")
        # Resets/increments the variables.
        result = []
        file_number += 1
        start += end
        end = start + number_of_lines

print("All done!")
time.sleep(5)
