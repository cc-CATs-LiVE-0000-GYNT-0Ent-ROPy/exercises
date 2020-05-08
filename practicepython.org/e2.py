def main():

  number = int(input('Whats your number? '))
  if number % 4 == 0:
    print("can be devided evenly by 4")
    pass
  elif number % 2:
    print("odd")
  else:
    print('even')

  num = int(input('Whats your number? '))
  check = int(input('Whats divider? '))
  if num % check:
    print("{} cant be divided by {}".format(num, check))
  else:
    print("{} can be divided by {}".format(num, check))


if __name__ == '__main__':
  main()
