'''https://www.practicepython.org/
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between 
the lists (without duplicates). Make sure your program works on two lists of different sizes.
Extras:
    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

import random


def common(a, b):
  out = []
  for i in a:
    if i in b:
      if i in out:
        pass
      else:
        out.append(i)
  return(out)

def main():
  a = sorted([random.randint(1, 99) for i in range(random.randint(1, 44))])
  b = [random.randint(1, 99) for i in range(random.randint(1, 44))]
  b.sort()
  print("list a {} ".format(a))
  print("list b {} ".format(b))

  out = common(a, b)
  print("out {} ".format(out))


if __name__ == '__main__':
  main()
