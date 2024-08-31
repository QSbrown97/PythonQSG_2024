#price variable stores string for coffee price
price = input("What is the price of a cup of coffee? ")

#cups variable stores string for amount of cups of coffee
cups = input("How many cups of coffee do you want? ")

#total variable stores the product of the price variable multiplied by the cups variable
# the price and cups variable have to be cast to their appropriate type in order to be multiplied 
total = float(price) * int(cups)

#print function prints out a string with total price for the provided amount of cups of coffee
print("Your total is $" + str(total) + " for " + cups + " cups.")