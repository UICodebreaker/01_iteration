#intial va
valid = False
#while loop
while not valid:
    try:
        number = int(input("Enter a number between 1 and 10:"))
        #if in range, end
        if number > 0 and number < 10:
            print(number)
            valid = True
        #else, repeat
        else:
            print("Number out of range")
    #if not number, repeat
    except ValueError:
        print("Invalid input.")
