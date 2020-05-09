''' https://www.practicepython.org/ 
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list
of only the first and last elements of the given list. For practice, write this code inside a function.
'''

def firstlast(list):
  out = []  
  out = [list[0],list[-1]]  
  #out = list[::len(list)-1]
  #print([list, list.reverse()][0])
  return(out)

def main():
  a = [5, 10, 15, 20, 25]
  print(firstlast(a))

if __name__ == "__main__":
  main()