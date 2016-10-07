my_name = 'Gary'
my_age = 22 #years
my_height = 72 #inches
my_weight = 190 #pounds
my_eyes = 'brown'
my_hair = 'brown'

# things like %s or %d embed the variable within them as they are called later on in the line
# the letter after the mod changes the context of the thing. %f makes it read in a float, for example
print "kets talk about %s" %my_name
print "he's %d inches tall" % my_height
print "he's %d pounds heavy" % my_weight
print "that's not too bad. he runs a bunch when his feet don't betray him"
print "he's got %s eyes and %s hair" % (my_eyes, my_hair)

print "if i add %s, %s, and %d, I end up with %s" % (my_age, my_height, my_weight, my_age + my_height + my_weight)
