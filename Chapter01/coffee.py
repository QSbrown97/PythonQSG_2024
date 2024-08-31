# ClydeBank Coffee Shop Simulator 4000
# Copyright (C) 2023 ClydeBank Media, All Rights Reserved.

print("ClydeBank Coffee Shop Simulator 4000, Version 1.00")
print("Copyright (C) 2023 ClydeBank Media, All Rights Reserved.\n")
print("Let's collect some information before we start the game.\n")

# Get name and shop name
name = input("What is your name? ")
shope_name = input("What do you want to name your coffee shop? ")

# Print name and pricing statement
print("\nThanks, " + name + ". Let's set some initial pricing.\n")

# Get initial price of a cup of coffee
cup_price = input("What do you want to charge per cup of coffee? ")

# Display all provided input
print("\nGreat. Here's what we've collected so far.\n")
print("Your name is " + name + " and you're opening " + shope_name + "!")
print("Your first cup of coffee will sell for $" + cup_price + ".\n")