import random
import math
secret_number = round(random.random() * 10)

attempts = 3

print("You have 3 attempts to guess the number")

for i in range(attempts):
 guess = int(input("Enter your guess: "))
 if guess > secret_number:
    print("Your guess is too high")
 elif guess < secret_number:
    print("Your guess is too low")
 else:
    print("Correct! You win!")
    break
else:
  print(f"You're out of attempts! The correct number was {secret_number}.")
print("Game over.")