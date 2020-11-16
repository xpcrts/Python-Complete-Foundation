# Read .txt file
# Use open() function to open a file 
f_txt = open("28_items.txt", "r")

# Use read() function to read the file
# Then print the read file
print(f_txt.read())

# Close the file
f_txt.close()


# Read .json file
# Use open() function to open a file 
f_json = open("28_friends.json", "r")

# Use read() function to read the file
# Then print the read file
print(f_json.read())
# Close the file
f_json.close()


# Read .csv file
# Use open() function to open a file 
f_csv = open("28_friends.csv", "r")

# Use read() function to read the file
# Then print the read file
print(f_csv.read())
# Close the file
f_csv.close()