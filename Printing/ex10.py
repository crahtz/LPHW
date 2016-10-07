tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backlash_cat = "I'm a \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

#It's weird because of the \r, which is the carriage return <CR> character
#in ascii. It basically resets the cursor to the start of the line.
#The comma at the end of that line is because in python 2.7,
#the print statement adds a newline. Using the comma, the newline is not added.
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
