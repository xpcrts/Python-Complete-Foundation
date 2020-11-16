# Import module
import re

# Initiate new variable
text = "Regular Expression Module is a module commonly uses to find, replace, search, split, characters/string."

# Using split() function
regex = re.split("\s", text)
print(regex)