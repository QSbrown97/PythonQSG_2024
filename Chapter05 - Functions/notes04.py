## Notes for Chapter 05 - Creating Reusable Tasks with Functions

# Functions allow us to reuse code
# We can pass arguments(parameters) to functions
# Keyword arguments make it easy to pass arguments
# DRY(Don't Repeat Yourself)

print("Ex: 5.01: Ask Function")
# Define the ask function
# def - statement used to define a function

def ask(prompt):
  return input(prompt + " ")

# Use the ask function to find out how many cups we want

print(ask("How many cups do you want?"))

## Passing values, returning results
# Argument - a value passed to a function

name = ask("What is your name?")
print(name)

print("Ex: 5.02: Multiple Args Function")
# Define the function full_name

def full_name(first, middle, last, display):
  name = first + " " + middle + " " + last
  if display:
    print(name)
  return name

# Executing full_name function

full_name("Quana", "S", "Brown", True)
complete_name = full_name("Quana", "S", "Brown", False)

print(complete_name)

## Modifying Arguments

print("Ex: 5.03: Modifying Args")

x = 5

def double(y):
  return y * 2

x = double(x)
print(x)

## Default Args
# Keep default args at the end of function definition

print("Ex: 5.04: Default Args")

def ask_default(prompt = "Please enter a value: "):
  if prompt.endswith(" "):
    return input(prompt)
  else:
    return input(prompt + " ")

a = ask_default()
b = ask_default("What do you want for b?")
print(a)

def full_name_default(
    first = "First",
    middle = "Middle",
    last = "Last",
    display = False):
  
  name = first + " " + middle + " " + last
  if display:
    print(name)
  return name

print(full_name_default)

## Keyword Args
# The order in which they're provided doesn't matter
# name each arg and specify their value, also good
# for functions that may expand later

print("Ex: 5.05: Keyword Args")

print(full_name_default(last = "Oliver", first = "Robert", middle = "W"))

## Arbitrary Args
# specify that a function can receive on or many args
# provide the name of a tuple as an arg

print("Ex: 5.06: Arbitrary Args")

# Define the average function
# * indicates an arbitrary arg
# len() - provides the total number of items

def average(*numbers):
  sum = 0
  for n in numbers:
    # Add n to sum
    sum += n
  return sum / len(numbers)

# Executing average function
print(average(10, 40, 80, 74, 16, 42, 12, 6))
# The result of a division operation is a float

## Scope
# the place where data structures and functions can be accessed
# Return - used to deliver a value back to the original scope

## Generator Functions
# run until it reaches a 'yield' statement, if called again it
# will pick up where it left off and continue to next 'yield'
# Refactor - restructuring or refining code

print("Ex: 5.07: Generator Functions")

# def infinity():
#   i = 0
#   while True:
#     yield i
#     i += 1

# for i in infinity():
#   print(i)

# Define bbsong generator
# start argument defaulting to 99

def bottles_song(start = 0):
  # Set the initial number of bottles to the start argument
  bottles = start
  # Loop through until bottles are gone
  while bottles < 100:
    # Display the song
    this_verse = []
    this_verse.append(str(bottles) + " bottles of beer on the wall.")
    this_verse.append(str(bottles) + " bottles of beer.")
    this_verse.append("Put one up, pass it around, ")
    # Subtract a bottle
    bottles += 1
    this_verse.append(str(bottles) + " bottles of beer on the wall.")
    # Yield to the calling function
    yield "".join(this_verse)
    # Pick back up here when we return
  return True

# Loop through the generator
for i in bottles_song():
  # Don't do anything as the generator does the printing
  print(i)

  # buffer - a place to temporarily store data
  # Pass = serves as code filler without taking action
  # it's a NOP(no-operation) statement, used to create time buffer