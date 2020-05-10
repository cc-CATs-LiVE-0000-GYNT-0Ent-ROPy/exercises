''' https://www.practicepython.org/ 
Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.
Extras:
    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
import random

def dedup1(xlist):
  return(list(set(xlist)))

def dedup2(xlist):
  out=[]
  for i in xlist:
    if i not in out:
      out.append(i)
  return(out)

def main():
  #xlist = [1, 1, 3, 3, 2, 2, 2, 3, 3, 4, 5, 6, 6]
  xlist = [random.randint(0,22) for i in range(random.randint(0,33))]
  print(sorted(xlist))
  print(sorted(dedup1(xlist)))
  print(sorted(dedup2(xlist)))

if __name__ == "__main__":
  main()