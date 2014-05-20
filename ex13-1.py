from sys import argv

script, = argv

print "The name of your script is:", script
response = raw_input("Would you like to change this name for this session?")

while response is not "yes":
    response = raw_input("Respond only with \"yes\" or \"no\".")


if response == "yes":
    script = raw_input("How would you like to rename it:")
    print "The name of your script is now:", script
elif response == "no":
    print "The name of your script hasn't change it's still:", script
else:
    print "WTF, you should have respond \"yes\" or \"no\"!!"

