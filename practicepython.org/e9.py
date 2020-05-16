import random
import sys


def userinput():
  usern = input("Whats your number of 1-9? ")
  if usern == "exit":
    print("Thank you for game")
    sys.exit()
  return int(usern)


def guess(y):
  counter = 0
  while True:
    x = userinput()
    counter += 1
    if x == y:
      print("You win after {}\n".format(counter))
      counter = 0
      break
    elif x > y:
      print("To high")
    else:
      print("To low")


if __name__ == '__main__':
  while True:
    print("Random number taken.")
    number = random.randint(1, 9)
    guess(number)

''' https://www.practicepython.org/ 
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
