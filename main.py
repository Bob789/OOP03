from rubberDuck import RubberDuck

# Create an instance of RubberDuck with the default quack_volume (5)
duck = RubberDuck()

# Print the duck object using the __str__ method
print(duck)  # Output: RubberDuck(quack_volume=5, color=yellow)

# Call the static method; does not require an instance
RubberDuck.squeak()  # Output: Squeak!

# Set a new quack_volume using the property setter
duck.quack_volume = 10

# Access the updated quack_volume using the property getter
print("New volume:", duck.quack_volume)  # Output: 10

# Increase the volume by 1 using static methode
duck.boost_volume()

# Print the new volume after boost
print("Boosted volume:", duck.quack_volume)  # Output: 11

# Access the default duck color using a class method
print("Default color:", RubberDuck.get_color())  # Output: yellow

# Set new color to hidden property
duck.set_color('Blue')

# After change color to new color
print("New color update:", RubberDuck.get_color())  # Output: Blue

duck2 = RubberDuck()
print("duck2 :", duck2 )



