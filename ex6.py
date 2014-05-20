# First sentence of a joke
x = "There are %d types of people." % 10
# First key word of the second sentence
binary = "binary"
# Second keyword of the second sentence
do_not = "don't"
# Second sentence of the joke
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the first sentence of the joke
print x
# Print the second sentence of the joke
print y

# Repeat the first part of the joke
print "I said: %r" % x
# Repeat the second part of the joke
print "I also said: '%s'." % y

# Response to the joke
hilarious = False
# Ask a question about the joke
joke_evaluation = "Isn't that joke so funny?! %r"

# Ask a question about the joke and respond.
print joke_evaluation % hilarious

# First part of a string
w = "This is the left side of..."
# second part of the string
e = "a string with a right side."

# Put the string together
print w + e
