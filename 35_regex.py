# Import module
import re

# Initiate new variable
text = "That cost around 20 bucks"

# Using \d special character
regex = re.findall("\d", text)
print(regex)