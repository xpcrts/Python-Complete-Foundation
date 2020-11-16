# Initiate new list 
var_list = [ 4, 10, 847, -2, 7, -5.378, 2, 38 ]

# Create our new function
def sort_list(mylist):
    for i in mylist:
        mylist.sort()
    print(mylist)
    return mylist

# call function 
sort_list(var_list)

