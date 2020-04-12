# This is all about class.

class house:
    """This class defines a house"""
    def house_stats (stats):
        """function to display your house stats."""
        print(f"My house has: \t{stats.floors} floors")
        print(f"My house has: \t{stats.bedrooms} bedrooms.")
        print(f"My house is: \t{stats.outside_color} on the outside.")
        print(f"My house is: \t{stats.inside_color} on the inside.")
        print(f"My house has: \t{stats.bathrooms} bathrooms.")

#loops until n is chosen
user_in = "y"
while user_in == "y":

    # creates an object (H1) that stores the users input.
    H1 = house()
    H1.floors = input("How many stories is your house?")
    H1.bedrooms = input("How many bedrooms does your house have?")
    H1.outside_color = input("What color/s is the outside of your house?")
    H1.inside_color = input("What color/s is/are the inside of your house?")
    H1.bathrooms = input("How many bathrooms are inside your house?")

    # runs the code
    H1.house_stats()
    user_in = input("Would you like to continue? y/n: ")
print("Goodbye.")