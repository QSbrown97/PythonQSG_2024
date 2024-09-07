from random import seed
from random import randint

def numberGame():
  number = randint(10, 100)

  while number > 0:

    print("Guess a number 10 through 100!")
    user_guess = input("What is your guess?: ")

    if user_guess != "exit":
      if int(user_guess) == number:
        print("Whoa you're right, the number is " + str(number))
      elif int(user_guess) != number:
        print("Nope, try again!")
        if number > int(user_guess):
          print("Go higher!")
        else:
          print("Go lower!")
    else: break

numberGame()