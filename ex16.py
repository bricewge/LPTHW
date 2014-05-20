# Request the package for using arguments
from sys import argv

# Name the arguments
script, filename = argv

# Informe the user that the file will be overwritten
print "We're going to erase %r." % filename
# Ask him if he want to continue and how to do so
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Wait for the user input
raw_input("?")

# Open the requested file to write in it
print "Opening the file..."
target = open(filename, 'w')

# Not needed because the file as been openend as writing
# Delete the information in the file
#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

# Ask the user to write the new 3 lines which would be inclued in the file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Write the new lines in the file
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# Close the file edited
print "And finally, we close it."
target.close()
