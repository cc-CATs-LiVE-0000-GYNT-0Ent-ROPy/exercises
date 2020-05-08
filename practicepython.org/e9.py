''' https://www.practicepython.org/ 
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random

def main():
  counter=0
  while True:
    number = random.randint(1,9)
    usern = input("Whats your number of 1-9? ")
    if usern == "exit":
      break
    else:
      usern = int(usern)

    print(number)
    counter += 1
    if number == usern:
      print("You win after {}".format(counter))
      counter = 0
    else:
      print("You lost")

  

if __name__ == '__main__':
  main()
