age = raw_input("How old are you? ")
# print "how old are you?",
# age = raw_input()
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

#watch out for %r with the height since both ' and " are involved potentially
print "so you're %r old, %s tall, and %r heavy." % (age, height, weight)
