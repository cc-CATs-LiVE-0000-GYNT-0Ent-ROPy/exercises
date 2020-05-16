import sys
import re


def namescount(f0):
  with open(f0, "r") as file:
    lines = file.read().splitlines()
    out = {n: lines.count(n) for n in lines}
  return out


def categorycount(f1):
  with open(f1, "r") as file:
    lines = file.read().splitlines()
    out = {}
    linesre = []
    for line in lines:
      linere = re.search('/.+/', line).group(0)
      linesre.append(linere)
      # print(linesre)
      out[linere] = linesre.count(linere)
  return out


if __name__ == "__main__":
  if len(sys.argv) == 1:
    f00 = "nameslist.txt"
    f01 = "training_01.txt"
  else:
    f00 = sys.argv[1]
    f01 = sys.argv[2]
  print("{} - {}".format(f00, namescount(f00)))
  print("{} - {}".format(f01, categorycount(f01)))

''' https://www.practicepython.org/
Given a .txt file that has a list of a bunch of names, count how many
of each name there are in the file, and print out the results to the
screen. I have a .txt file for you, if you want to use it!
Extra:
http://www.practicepython.org/assets/nameslist.txt
http://www.practicepython.org/assets/Training_01.txt
  Instead of using the .txt file from above (or instead of, if you
  want the challenge), take this .txt file, and count how many of
  each “category” of each image there are. This text file is
  actually a list of files corresponding to the SUN database scene
  recognition database, and lists the file directory hierarchy for
  the images. Once you take a look at the first line or two of the
  file, it will be clear which part represents the scene category.
  To do this, you’re going to have to remember a bit about string
  parsing in Python 3. I talked a little bit about it in this post.


f="/yyy/foobar/sun.jpg" ; echo ${f%sun*}
echo "/yyy/foobar/sun.jpg" | grep -oE "/.+?/"
echo "/yyy/foobar/sun.jpg" | awk '{match($1,"^.+?/",a)} {print a[0]}' /yyy/foobar/
echo "/yyy/foobar/sun.jpg" | awk '{match($1,"/.+?/",a)} {print a[0]}' /yyy/foobar/
echo "/yyy/foobar/sun.jpg" | awk '{match($1,"/[^/]+/",a)} {print a[0]}' /yyy/


echo "/yyy/foobar/sun.jpg" | grep -oE "/.+/" - greedy /yyy/foobar/
echo "/yyy/foobar/sun.jpg" | grep -oP "^.+?/"   - none greedy /yyy/

while read l; do echo ${l%sun*}; done < training_01.txt | uniq | wc -l
while read -r l; do echo "${l##*/}"; done < training_01.txt
'''
