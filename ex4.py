# Number of cars available
cars = 100 
# How many people can fillup a car
space_in_a_car = 4.0
# Number of drivers available
drivers = 30
# Number of passagenrs to transport
passengers = 90
# Cars nto driven
cars_not_driven = cars - drivers
# Cars driven
cars_driven = drivers
# Total of the cars available
carpool_capacity = cars_driven * space_in_a_car
# Average number of people in a car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each cars."
