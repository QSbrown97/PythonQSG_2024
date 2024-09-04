# Notes for Chapter 03 - Controlling Program Flow

## Logical Comparisons
# if = do something if this condition is met
# commands need to be indented
# else

a = "Yes"
b = "No"

if a == b:
  print("a is equal to b")
else:
  print("a is not equal to b")

# < - less than operator
# > - greater than operator

a = 1
b = 2
c = 3

if a < b:
  print("a is less than b")

# elif - else if, good for comparing in a chain
#*all else statements must appear after elif statements

if a > b:
  print("a is greater than b")
if c < b:
  print("c is less than b")
elif b < c:
  print("b is less than c")