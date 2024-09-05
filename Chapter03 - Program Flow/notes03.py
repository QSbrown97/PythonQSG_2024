# Notes for Chapter 03 - Controlling Program Flow

## Logical Comparisons
# if = do something if this condition is met
# commands need to be indented
# else

a = "Yes"
b = "No"

print("Ex: 3.01: else statement")
if a == b:
  print("a is equal to b")
else:
  print("a is not equal to b")

# < - less than operator
# > - greater than operator

a = 1
b = 2
c = 3

print("Ex: 3.02: Comparison")
if a < b:
  print("a is less than b")

# elif - else if, good for comparing in a chain
#*all else statements must appear after elif statements

print("Ex: 3.03: elif statement")
if a > b:
  print("a is greater than b")
if c < b:
  print("c is less than b")
elif b < c:
  print("b is less than c")

## Nested Comparison
# Comparisons can be nested creating complex logical comparisons
# != - Not equals
# >= - Greater than or equal to
# <= - Less than or equal to

print("Ex: 3.04: Nested Comparison")
if a > b:
  print("a is greater than b")
  if b != c:
    print("but b is not equal to c")
  else:
    print("b is equal to c")
else:
  print("a is less than b")

## Loops
# a loop is a piece of code that is executed repeatedly until a condition is met
# iterating - moving through a collection of data in a loop
# for - versatile, used to repeat code a specific amount of times

print("Ex: 3.05: for loop")
planets = [
  "Mercury",
  "Venus",
  "Earth",
  "Mars",
  "Jupiter",
  "Saturn",
  "Uranus",
  "Neptune"]

for planet in planets:
  print(planet)

greeting = "Hello World!"

print("Ex: 3.06: for loop")
for greet in greeting:
  print(greet)

print("Ex: 3.07: Modifying variable in a loop")

singular_words = ["student", "teacher", "room"]
for word in singular_words:
  print(word + "s")
else:
  print("Done!")

## Range
# a function used to iterate over a range of numbers
# argument - a value that is supplied to a function
print("Ex: 3.08: Range")

for i in range(10):
  print(i)

#enumerating - a variable used to track the position of a list

print("Ex: 3.09: Enumerating")

for index, value in enumerate(planets):
  print("Planet " + str(index + 1) + ": " + value)

# while - iterates loop as long as comparison evaluates to true
# while i is less than 10, display i
# incrementing - increasing a variable
# decrementing - decreasing a variable

print("Ex: 3.10: while loop")

i = 0
while i <= 10:
  print(i)
  i += 1

print("Ex: 3.11: Beer Song - while loop")

bottles = 99
while bottles > 0:
  print(str(bottles) + " bottles of beer on the wall.")
  print(str(bottles) + " bottles of beer.")
  bottles -= 1
  print("Take one down, pass it around,")
  print(str(bottles) + " bottles of beer on the wall")

print("Ex: 3.12: Beer Song - for loop")
more_bottles = 99

for i in range(more_bottles):
  if more_bottles > 0:
    print(str(more_bottles) + " bottles of beer on the wall.")
    print(str(more_bottles) + " bottles of beer.")
    more_bottles -= 1
    print("Take one down, pass it around")
    print(str(more_bottles) + " bottles of beer on the wall")

## Break
# used to conditionally exit a loop before it is finished

print("Ex: 3.13: Break statement")
while True:
  print("Hello, World!")
  break

print("Ex: 3.14")
for i in range(10):
  print(i)
  if i >= 5: break

## Continue
# allows us to skip the current iteration and move ->
# to the next without exiting the loop
# Modulo/Mod operator (%) - performs division and returns the remainder, odd or even

print("Ex: 3.15: Continue statement")

for i in range(10):
  if i % 2: continue
  print(i)

## Nested Loops
# Loops can exist within themselves
print("Ex: 3.16: Nested Loops")

for i in range(10):
  for j in range(10):
    print(str(i) +":" + str(j))