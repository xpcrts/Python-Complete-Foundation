try:
    number = int(input("Enter any number: "))
    print(number)
except:
    print("Invalid input, input must be an integer")
finally:
    print("Please rerun your program")