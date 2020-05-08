''' https://www.practicepython.org/ 
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, 
described below.
'''
from e4 import divisors

def main():
  number=int(input("Prime number? "))
  if not divisors(number):
    print("Prime")
  else:
    print("Not prime")

if __name__ == "__main__":
  main()