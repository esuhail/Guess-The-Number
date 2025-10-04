import random

print("Guess the Number (1-100)")

secret = random.randint(1,100)

tries = 0

done = False

while done == False:
  guess_text = input("Enter your guess: ")

guess = int(guess_text)

if guess < 1 or guess > 100:
  print("Number must be between 1 and 100!")
else:
  tries = tries + 1

if guess == secret:
  print("Correct! you got it in", tries, "tries.")
  done = True
elif guess < secret:
  print("Too low!")
else:
  print("Too high!")

difference = secret - guess
if different < 0:
  difference = difference * -1
if difference <= 10 and guess != secret:
  print("You're very close!")
elif difference <= 25 and guess != secret:
  print("You're getting warmer.")
elif guess != secret:
  print("Freezing cold! Try again.")

print()
  
