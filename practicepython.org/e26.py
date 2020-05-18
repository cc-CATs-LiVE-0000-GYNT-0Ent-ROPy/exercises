import numpy as np

def tictactoe(game):
  win = 0
  if win < 1:
    win = diagonal(game)
  if win < 1:
    win = line(game)
  gamerot = np.rot90(game)
  if win < 1:
    win = diagonal(gamerot)
  if win < 1:
    win = line(gamerot)
  return win

def diagonal(game):  
  out = 0
  res = 0
  size = len(game[1])
  #print(np.array(game))
  for i in range(size-1):
    if game[i][i] == game[i+1][i+1]:
      out += 1
    if out == size - 1:
      res = game[i][i]
      break
  return res

def line(game):
  out = 0
  res = 0
  size = len(game[1])
  #print(np.array(game))
  for i in range(size):
    for j in range(size -1):
      if game[i][j] == game[i][j+1]:
        out += 1
    if out == size - 1:
      res = game[i][j]
      break
    out = 0
  return res

if __name__ == "__main__":
  game2 = [[1, 2, 0],
           [2, 1, 0],
           [2, 1, 1]]

  game  = [[1, 2, 2, 2],
           [1, 1, 2, 1],
           [2, 2, 1, 1],
           [2, 1, 0, 1]]

  print(tictactoe(game))


''' https://www.practicepython.org/
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The 
other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full 
tictactoe board. However, this is significantly more than half an 
hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON 
a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
  [2, 1, 0],
  [2, 1, 1]]

where a 0 means an empty square, a 1 means that player 1 put their 
token in that space, and a 2 means that player 2 put their token in 
that space.

Your task this week: given a 3 by 3 list of lists that represents 
a Tic Tac Toe game board, tell me whether anyone has won, and tell me 
which player won, if any. A Tic Tac Toe win is 3 in a row - either in 
a row, a column, or a diagonal. Don’t worry about the case where TWO 
people have won - assume that in every board there will only be one 
winner.

Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],
  [2, 1, 0],
  [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
  [2, 1, 0],
  [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
  [2, 1, 0],
  [2, 1, 1]]

no_winner = [[1, 2, 0],
  [2, 1, 0],
  [2, 1, 2]]

also_no_winner = [[1, 2, 0],
  [2, 1, 0],
  [2, 1, 0]]

game_1 = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
game_2 = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
game_3 = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
game_4 = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
game_5 = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
game_6 = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]

'''
