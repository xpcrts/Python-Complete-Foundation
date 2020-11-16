# Use open() function to open a file 
f = open("30_newfile.txt", "w+")
# Use write() function to write the file
f.write("I am just created a new file.")
# Close the file
f.close()