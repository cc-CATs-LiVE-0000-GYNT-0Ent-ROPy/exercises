''' https://www.practicepython.org/ 
Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
Extra:
    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import random
import sys

def passwordgen(x):
  out = ''.join([chr(random.randint(33,127)) for i in range(x)])
  return out

def main():  
  x = int(sys.argv[1])
  #x = int(input("Password complicity? "))

  if x<4:
    print(random.choice(['win', 'lose', 'draw', "qaz", "wsx"]))
  elif x<8:
    print(random.choice(['win', 'lose', 'draw', "qaz", "wsx"])+random.choice(['win', 'lose', 'draw', "qaz", "wsx"]) )
  else:
    print(passwordgen(x))

if __name__=="__main__":
  main()