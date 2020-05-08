# https://www.practicepython.org/ Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def main():
  length = len(word)
  j = 0
  for i in range(length // 2):
    if word[i] == word[length - 1 - i]:
      j += 1
    else:
      break

  if j == length // 2:
    print("palindrome")
  else:
    print("not palindrome")


def oneliner():
  print("is palindrome? ".format(word == word[::-1]))


if __name__ == '__main__':
  for x in range(1000000):
    word = input("Give me a word: ")
    main()
    oneliner()
