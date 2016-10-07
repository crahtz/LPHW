formatter  = "%r %r %r %r"
# note: %r gives the raw text of a variable, so it isn't deisnged to be seen
# by a user. that's what %s or something would be for

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)

#gosh isn't this one cheecky
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing",
"That you could type up right",
"but it didn't sing",
"so i said goodnight"
    )


#remember that ctrl /  lets you make a whole bunch of shit a comment

days = "mon tue wed thu fri sat sun"

# the \n throws the next part of the string onto another line
months = "jan\nfeb\nmar\napr\nmay\njune\njul\naug"

print "here are the days: ", days
print "here are some of the months: ", months

# note how the result of this is jan\nfeb\nmar\napr\nmay\njune\njul\naug
print "there's also this: %r" % months

# by using triple quotes, you can throw whatever you want into your string
print """
    There's something going on here.
    With three double-quotes
    We can type as much as we like
    Cuz there aren't any spaces between each quotation mark
    Cuz syntax
    """
