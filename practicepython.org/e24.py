import sys


def row(n):
  out1 = " "
  out2 = ""
  for i in range(n):
    out1 += "--- "
    out2 += "|   "
  print("{}\n{}| ".format(out1, out2))


def board(n):
  out1 = " "
  for i in range(n):
    row(n)
    out1 += "--- "
  print(out1)
  return ""


if __name__ == "__main__":
  if len(sys.argv) > 1:
    # print(row(int(sys.argv[1])))
    print(board(int(sys.argv[1])))
  else:
    print("use: python e24.py 3")

''' https://www.practicepython.org/
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. 
The other exercises are: Part 2, Part 3, and Part 4.
Time for some fake graphics! Let’s say we want to draw game boards 
that look like this:
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many 
other sizes (8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for 
them to the screen using Python’s print statement.
'''
