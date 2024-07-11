import random

def guess_number(tries):
  number = random.randint(1, 100)
  guess_count = 0

  while guess_count < tries:
    guess = int(input("Guess a number between 1 and 100: "))
    guess_count += 1

    if guess > number:
      print("Too big!.")
    elif guess < number:
      print("Too small!")
    else:
      print(f"You guessed in {guess_count} tries! The number was {number}.")
      return

  print(f"You ran out of guesses. The number was {number}.")


tries = 5
guess_number(tries)
