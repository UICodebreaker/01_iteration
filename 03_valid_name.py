valid = False

while not valid:
    name = input("Enter a name: ")
    if name == "":
        print("Name cannot be left blank.")
    else:
        valid = True
        print("Stored name: {}".format(name))
