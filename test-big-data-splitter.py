from itertools import islice
import time

#Prompting / instructions

print("Lets split some files today!")
print("Make sure that I'm in the same directory as the file you want to split!")



################# VARIABLES TO CHANGE #################

# File to split (This is going to be your HUGE json file)
file_to_split = input("What file are we splitting today? (Please add the file extension): ")

# This is going to be the "base" file name for all your new files. Make it meaningful!
filename = input("What's the base name of our new files? ")

# This is how your files are going to be saved
extension = input("What extension should I be making the new files? (example: .json): ")

# This is how many files you want
desired_file_number = int(input("How many new files would you like to create in total? "))

# This is how many lines you want
number_of_lines = int(input("How many lines do you want each file to be of the file_to_split? "))


#######################################################

print("Hang tight, I'll get started")




################# Below is the magic #################

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

    for file_count in itertools.count(1):
            out_filename = '{}_{}_{}{}'.format(file_count,filename,)
            with open(out_filename, 'w') as outfp:
                oufp.writelines(itertools.islice(inputfile,number_of_lines))
                print("File {} done...").format(file_count)
            if os.stat(out_filename).st_size == 0:
                os.remove(out_filename)
                break

print("All done!")
time.sleep(5)