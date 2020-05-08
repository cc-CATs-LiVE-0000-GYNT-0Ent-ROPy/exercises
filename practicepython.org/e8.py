''' https://www.practicepython.org/ 
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''
import random

def rock(computer):
  if computer=="rock":
    print("draw")
  elif computer=="scissors":
    print("You win")
  else:
    print("You lost")

def paper(computer):
  if computer=="rock":
    print("You win")
  elif computer=="scissors":
    print("You lost")
  else:
    print("draw")

def scissors(computer):
  if computer=="rock":
    print("You lost")
  elif computer=="scissors":
    print("draw")
  else:
    print("You win")  

def nothing(computer):
  print("wrong input")

def main():
  switcher = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
  }

  items = ["rock", "paper", "scissors"]
  player = str(input("Give one of rock, paper, scissors: "))
  computer = items[random.randint(0, 2)]
  print("computer: {}".format(computer)) 

  func=switcher.get(player, nothing)
  return func(computer)


if __name__ == '__main__':
  main()
