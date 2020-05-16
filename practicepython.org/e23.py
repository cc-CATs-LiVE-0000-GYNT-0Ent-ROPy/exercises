import sys


def overlapping(f1, f2):
  with open(f1, "r") as file1, open(f2, "r") as file2:
    f1l = [n for n in file1.read().splitlines()]
    print(f1l)
    f2l = [n for n in file2.read().splitlines()]
    print(f2l)
    out = [n for n in f1l if n in f2l]
    return(out)


if __name__ == "__main__":
  if len(sys.argv) == 3:
    print(overlapping(sys.argv[1], sys.argv[2]))
  else:
    print("use: python e23.py primenumbers.txt happynumbers.txt")

''' https://www.practicepython.org/

http://www.practicepython.org/assets/primenumbers.txt
http://www.practicepython.org/assets/happynumbers.txt

Given two .txt files that have lists of numbers in them, find the 
numbers that are overlapping. One .txt file has a list of all prime 
numbers under 1000, and the other .txt file has a list of happy 
numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by 
any other number. And yes, happy numbers are a real thing in 
mathematics - you can look it up on Wikipedia. The explanation 
is easier with an example, which I will describe below.)
'''
