
def maxx():
  print(sorted(li)[-1])

if __name__ == "__main__":
  inp = input("Give three integers space separated: ")
  li = [int(i) for i in inp.split()] 
  maxx()
''' https://www.practicepython.org/
Implement a function that takes as input three variables, and returns 
the largest of the three. Do this without using the Python max() 
function!
The goal of this exercise is to think about some internals that Python
 normally takes care of for us. All you need is some variables and if 
 statements!
'''
