from random import seed
from random import randint

number = randint(1, 10)
while number > 0:
  print("Guess a number 1 through 10!")
  user_guess = input("What is your guess?: ")
  if int(user_guess) == number:
    print("Whoa you're right, the number is " + str(number))
    break
  else:
    print("Nope, try again!")