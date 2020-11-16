# Import module
import re

# Initiate new variable
text = "That cost around 20 bucks"

# Using ^ special character
regex = re.findall("^That", text)

if regex:
    print("Data found")
else:
    print("Not found")