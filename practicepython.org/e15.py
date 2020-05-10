''' https://www.practicepython.org/ 
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
'''
def reversewords(sentence):
  out = sentence.split(' ')
  out.reverse()
  return(' '.join(out))


def main():
  sentence=input('Give sentence: ')
  print(reversewords(sentence))

if __name__ == "__main__":
  main()
