# -- coding: utf-8 --
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d cm (%d inches) tall." % (height * 2.54, height)
print "He's %d kg (%d pounds) heavy." % (weight * 0.45359237, weight)
print "Actually that' not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usuallt %s depending of the cofee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
