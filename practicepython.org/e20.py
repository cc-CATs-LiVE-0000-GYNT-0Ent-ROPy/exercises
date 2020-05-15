import sys
import random

def binarysearch(n, l):
  L = 0 
  R = len(l)-1
    #print(l[L],"->",n,"<-", l[R])
  while L <= R :
    idx = R - (R-L)//2
    mid = l[idx]
    print("{}-{}".format(idx,mid))
    if n == mid:
      return "wynik: {} ".format(n)
    elif n > mid:
      L = idx + 1
      #print("{}-{} >>> {}-{}".format(L,l[L],R,l[R])) 
      #may cause error - index overflow 
    else:
      R = idx - 1
      #print("{}-{} <<< {}-{}".format(L,l[L],R,l[R]))

  return "brak"

def main():
  l0 = sorted(random.sample(range(0,20), 11))
  n0 = int(sys.argv[1])
  print(l0)
  print(binarysearch(n0, l0))

if __name__ == "__main__":
  main()

''' https://www.practicepython.org/ 
Write a function that takes an ordered list of numbers (a list where 
the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list 
and returns (then prints) an appropriate boolean.
Extras:
    Use binary search.
'''