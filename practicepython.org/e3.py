# https://www.practicepython.org/

def main():

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  number = int(input('Whats your number? '))

  for i in a:
    if i <= number:
      pass
    else:
      break

  print(a[:a.index(i)])

  # oneliner
  print([aa for aa in a if aa <= number])


if __name__ == '__main__':
  main()
