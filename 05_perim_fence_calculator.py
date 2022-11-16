    # functions go here

# checks input is a number more than zero
def num_check(question):
    Valid = False
    while not Valid:


        error = "Please enter number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more then zero
            if response > 0:
                return response

            # output error if input is invalid
            else:
                print(error)
                print ()

        except ValueError:
            print (error)




# Main Routine goes here

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area (width x height)
    area = width * height 

    # Calulate perimeter (width + height) x 2
    perimeter = 2 * (width + height)

    # Output area and perimeter
    print("perimeter: {} units".format(perimeter))
    print("Area: {} square units". format(area))
    print()
    keep_going = input("Press <enter> to keep going or any key to quit")




print()
print("Thanks for using the area / perimeter calculator")

