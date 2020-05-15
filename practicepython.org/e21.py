import sys
import e17


def savefile(filename):
  with open(filename, 'w') as open_file:
    open_file.write(str(e17.scraper("http://interia.pl", "a")))
  return false


if __name__ == "__main__":
  if len(sys.argv) == 1:
    f = input("Give filename? ")
  else:
    f = sys.argv[1]
  savefile(f)

''' https://www.practicepython.org/ 
Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, 
use the code from the solution 17), and instead of printing 
the results a screen, write the results to a txt file. In your code, 
just make up a name for the file you are saving to.
Extras:
    Ask the user to specify the name of the output file that will be 
    saved.
'''
