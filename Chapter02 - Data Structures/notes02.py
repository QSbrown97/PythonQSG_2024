# Notes for Chapter 2 - Data Structures

# Picking the Right Data Structure
# Lists - go-to solution for storing collection of data, default
# Sets - faster than lists in some cases
# Tuples - performance critical, data won't change
# Dictionaries - complex data, possible additions of data

## Lists [] - a data structure that contains multiple variables

grocery_list = ["eggs", "milk", "cheese", "pasta"]

planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

odd_numbers = [1, 3, 5, 7, 9]

random_assortment = ["egg", "tree", 3, "green", 94, "Pluto", 3.14]

# referencing an element in a list
# index - the number used to access an item
# memory location calculated by first_address + (index x length)

print("The first item on the list is " + grocery_list[0])
print("The second item on the list is " + grocery_list[1])

## Tuples () - Similar to Lists but cannot be changed (immutable)
# Tuples are good for predefined sets of data because they're safer, faster, and use less memory
# immutable variable are read-only, whereas mutable data is editable

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

# accessing an element of the planets tuple
print(planets[3])

## Sets {}(unordered) - similar to a List but only contains unique values, good for deduplicating data
# This is good for less memory and disk space consume, as well as improved performance

customers = {
            "James Smith",
            "Andrea Richards",
            "Sam Sharp",
            "Brenda Longmire",
            "Veronica March",
            "Sylvia Smith",
            "James Smith",
            "Vanessa Bush",
            "Steve Hammersmith",
            "Brenda Longmire",
            "Sylvia Smith",
            "Steve Hammersmith",
            "Walt Hawkins"
            }
# printing customers set
print(customers)

## Dictionaries {} (mutable) - indexed Lists of values that don't allow duplicates
# key-value pair - a way to reference a piece of data that has a key or index attached to it

customer1 = {
          
          "name": "James Smith",
          "age": 24,
          "phone": "555-555-1941",
          "email": "james@xyzinternet.net"
}

customer2 = {

          "name": "Andrea Richards",
          "age": 33,
          "phone": "555-555-4928",
          "email": "andrea@coffeeloversunite.us"
}

customer3 = {
          "name": "Robert",
          "name": "John"
}

# accessing and printing a value from a dictionary

print(customer1["name"])
print(customer3["name"])

## Boolean Variables - True/on or False/off

walking = False
running = True

## Combining Data Structures
# Multidimensional Lists - Lists of lists

# Daily high and low temperature (in Fahrenheit)
temps = [
  [
    [66, 34],
    [57, 25],
    [49, 45],
    [45, 19],
    [33, 7],
    [32, 14],
    [49, 37]
  ],
  [
    [53, 39],
    [61, 51],
    [64, 51],
    [67, 57],
    [69, 42],
    [32, 14],
    [49, 37]
  ]
]

# Day 1 temps
print(temps[0])
# Day 2 temps
print(temps[1])
# Day 3 temps
#print(temps[2])

# Day 1 high
print(temps[0][0])
# Day 1 low
print(temps[0][1])

# Week 2 Day 3 low
print(temps[1][2][1])