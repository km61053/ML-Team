import random
n = random.randint(1, 5)
guess = int(input("Enter an integer from 1 to 5: "))
while n != "guess":
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 5: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 5: "))
    else:
        print ("you guessed it!")
        break
