import random

print("Guess the Number (1-100)")
secret = random.int(1,100)
tries = 0

while True:
  guess_text = input("Enter your guess: ")

if guess_text != int:
  print("Please enter a whole number only!")
  continue
  
if guess < 1 or guess > 100:
  print("Number must be between 1 and 100!")
  continue

tries += 1

if guess == secret:
  print(f" Correct! {guess} was the number. It took you {tries} tries.")
  break

elif guess < secret:
  print("Too low!")
else:
  print("Too high!")

difference = abs(secret - guess)

if difference <= 10:
  print("You're very close!")
elif difference <= 25:
  print("You're getting warmer.")
else:
  print("Freezing cold! Try again.")

print()
  
