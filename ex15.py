# Import module to use arguments
from sys import argv

# Name the arguments passed to the script
script, filename = argv

# Store the file in the variable named txt
txt = open(filename)

# Print out the file
print("Here's your file %r:" % filename)
print(txt.read())
txt.close()

# Ask a other filename
print("Type the filename again:")
file_again = raw_input("> ")

# Open the other file
txt_again = open(file_again)

# Read that other file
print(txt_again.read())
txt_again.close()
