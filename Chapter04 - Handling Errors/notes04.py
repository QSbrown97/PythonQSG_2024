## Notes for Chapter 04 - Handling Errors

# An exception occurs when an error happens
# which can be handled with the 'try' statement

# When a problem occurs in the try block, code
# in the except block is run

# If no error occurs, code in the 'else' blocks
# is run, but is skipped if something is wrong

# The 'finally' block is executed in either case
# and is commonly used to restore program's exec-
# ution to a sane state


# Wrapping code in 'try' provides a safety harness against failure
# The finally statement ensures that code is run even if an error occurs

## Exceptions
# when an error occurs / throws an exception

## Python Exception-handling process
# 'try' - try to run this code
# 'except' - run this code when something goes wrong
# 'else' - everything went fine, so run this
# 'finally' - no matter what happens, run this code

print("Ex: 4.01: Exception handling")

# Divide a number by zero
a = 7
b = 0

try:
  print(str(a) + " divided by " + str(b) + " is " + str(a / b))

  # when not sure what exception may happen use 'Exception'
except Exception as e:
  print("Sorry, a problem occurred dividing the numbers")
  # cast 'e' to a string because is and 'Exception(class)' type by default
  print("Error details: " + str(e))
finally:
  print("But still we tried!")

print("All done!")