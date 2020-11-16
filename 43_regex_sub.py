# Import module
import re

# Initiate new variable
text = "Regular Expression Module is a module commonly uses to find, replace, search, split, characters/string."

# Using sub() function
regex = re.sub("\s", "xxx", text)
print(regex)