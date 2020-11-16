# Import module
import re

# Initiate new variable
text = "Regular Expression Module is a module commonly uses to find, replace, search, split, characters/string."

# Using \s special character
regex = re.findall("\s", text)
print(regex)

if regex: 
    print("There are spaces contain in the string.")
else:
    print("Space not found")