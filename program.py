# HTTPS://WWW.W3RESOURCE.COM/PYTHON-EXERCISES/PYTHON-BASIC-EXERCISES.PHP

# MY ATTEMPT
# # Used for exacting file extension
# import os
#
# # Prompt user to create file
# create_file = input("Create a file with the filename and extension(ex. file.txt): ")
#
# # Program displays filename
# print("Sample file: ")
#
# # Program creates the file based on the user input
# new_file = open(create_file, "x")
#
# # Used for exacting file extension
# print("File extension: ", os.path.splitext(new_file))
#
# # Removes the file at the end of the program
# os.remove(create_file, new_file)

###############################################################################

# At this point, I had been working on this exercise for days trying to figure
# out how to do this correctly and finally decided to quit and just look at the
# solution.

###############################################################################

# CORRECT SOLUTION
import os

filename = input("Input the Filename: ")
print("Sample file: ", filename)     # My addition
f_extns = filename.split(".")
print ("Output: " + repr(f_extns[-1]))

# Gives the user the option to delete the file and checks if it already exists
# NOTE: I did not realize until after making this block of code that the
# program does not save the file inputted by the user.
# rm_file = input("Do you want to remove the file? (y/n)")
# if rm_file == "y":
#     # Source: https://www.w3schools.com/python/python_file_remove.asp
#     if os.path.exists(filename):
#         os.remove(filename)
#     else:
#         print("The file does not exist")