# Import module
import re

# Initiate new variable
text = "Regular Expression Module is a module commonly uses to find, replace, search, split, characters/string."

# Using + special character
regex = re.findall("mo+", text)
print(regex)