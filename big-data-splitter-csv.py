import itertools
import time
import os

print("Lets split some files today!")
print("Make sure that I'm in the same directory as the file you want to split!")

################# VARIABLES TO CHANGE #################

# File to split (This is going to be your HUGE json file)
file_to_split = input("What file are we splitting today? (Please add the file extension): ")

# This is going to be the "base" file name for all your new files. Make it meaningful!
filename = input("What's the base name of our new files? ")

# This is how many lines you want
number_of_lines = int(input("How many lines do you want each file to be of the file_to_split? "))

#######################################################

print("Hang tight, I'll get started...")




################# Below is the magic #################

with open(file_to_split) as infp:
    # file counter used to create unique output files
    for file_count in itertools.count(1):
        out_filename = '{}_{}_{}.csv'.format(file_count, filename, number_of_lines)
        with open(out_filename, 'w') as outfp:
            # write configured number of lines to file
            outfp.writelines(itertools.islice(infp, number_of_lines))
         # break when no extra data written
        if os.stat(out_filename).st_size == 0:
            os.remove(out_filename)
            break
            
print("All done!")
time.sleep(5)