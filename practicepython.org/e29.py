import sys
import numpy as np

def tictactoe(game):
  #print(np.array(game))
  board(3)
  win1 = '0'
  if win1 == '0':
    win1 = diagonal(game)
  if win1 == '0':
    win1 = line(game)
    #print("returned {} {} {}".format(win1, type(win1), win1 == '0'))
  if win1 == '0':
    #print("diagonal rot")
    win1 = diagonal(np.rot90(game))
  if win1 == '0':
    win1 = line(np.rot90(game))
  return win1

def diagonal(game):  
  out = 0
  res = '0'
  size = len(game[1])
  #print(np.array(game))
  for i in range(size-1):
    if game[i][i] == game[i+1][i+1] and game[i][i] != '0':
      out += 1
      #print("di {} {} {}".format(i, game[i][i],out))
    if out == size - 1:
      res = str(game[i][i])
      break
  return res

def line(game):
  out = 0
  res = '0'
  size = len(game[1])
  #print(np.array(game))
  #print(game,"\n")
  for i in range(size):
    for j in range(size -1):
      if game[i][j] == game[i][j+1] and game[i][j] != '0':
        out += 1
        #print("li {} {} {}".format(i, game[i][j],out))
    if out == size - 1:
      res = str(game[i][j])
      #print("res {}".format(res))
      break
    out = 0
    #print("next")
  return res

def board(n):
  out1 = out2 = out3 = ""
  i = j = 0
  for i in range(n):
    for j in range(n):
      out1 += " ---"
      out2 += "| {} ".format(game[i][j])
    print("{}\n{}| ".format(out1, out2))
    out1 = out2 = ""
    out3 += " ---"
  print(out3)
  return ""

def move(game):
  win1 = "0"
  turn = 0
  while (win1 == "0" and turn <= 9):
    if win1 == "0":
      turn += 1
      p = input("P1 move: ")
      slot = game[int(p[0])][int(p[2])]
      if slot == '0':
        game[int(p[0])][int(p[2])] = "X"
      else:
        print("occupied - you lost turn")
      win1 = tictactoe(game)
    if win1 == "0":
      turn += 1 
      #print(game)
      p = input("P2 move: ")
      slot = game[int(p[0])][int(p[2])]
      if slot == "0":
        game[int(p[0])][int(p[2])] = "O"
      else:
        print("occupied - you lost turn")
      win1 = tictactoe(game)
  return "The winner is: {} ".format(win1)

def drawboard(game):
  pass

if __name__ == "__main__":
  game3 = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
  
  game2 = [[0, 0],
          [0, 0]]
  game = np.array(game3, str)
  print(move(game))

''' https://www.practicepython.org/
This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The 
other exercises are: Part 1, Part 2, and Part 3.

In 3 previous exercises, we built up a few components needed to build 
a Tic Tac Toe game in Python:
    Draw the Tic Tac Toe game board
    Checking whether a game board has a winner
    Handle a player move from user input
The next step is to put all these three components together to make a 
two-player Tic Tac Toe game! Your challenge in this exercise is to use
 the functions from those previous exercises all together in the same 
 program to make a two-player game that you can play with a friend. 
 There are a lot of choices you will have to make when completing this
  exercise, so you can go as far or as little as you want with it.
Here are a few things to keep in mind:
    You should keep track of who won - if there is a winner, show a 
    congratulatory message on the screen.
    If there are no more moves left, don’t ask for the next player’s 
    move!
As a bonus, you can ask the players if they want to play again and 
keep a running tally of who won more - Player 1 or Player 2.
'''
