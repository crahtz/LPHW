# Make a new directory:
# New-Item -ItemType directory -Path c:\whatever
# mkdir \whatever #(in this case within C:\, so C:\whatever now exists!!)
#
# Change a directory:
# cd \whatever

# List the files within directory
# Get-ChildItem C:\whatever

# the comma keeps the result of line 12 on the same line as the code from line 13
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#note, the result of this will be one, since the decimal is rounded to the nearest whole
print (9/5)

# things like %s or %d embed the variable within them as they are called later on in the line
# the letter after the mod changes the context of the thing. %f makes it read in a float, for example
print "let's talk about %s" %my_name

# note: %r gives the raw text of a variable, so it isn't deisnged to be seen
# by a user. that's what %s or something would be for
formatter  = "%r %r %r %r"

# Escape sequences:
# the \n throws the next part of the string onto another line
# using \t tabs what's about to come
# https://learnpythonthehardway.org/book/ex10.html
months = "jan\nfeb\nmar\napr\nmay\njune\njul\taug"

# by using triple quotes (either """ or '''), you can throw whatever you want into your string
print """
    kjsgnfad
    kajgnf
    """
