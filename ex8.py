# The format of the string we'll use here.
formatter = "%r %r %r %r"

# Print the fist four numbers
print formatter % (1, 2, 3, 4)
# Print literally the first four numbers
print formatter % ("one", "two", "three", "four")
# Print
print formatter % (True, False, False, True)
# Print four times the sring formatter
print formatter % (formatter, formatter, formatter, formatter)
# Print on one line a four line strings.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight"
)
