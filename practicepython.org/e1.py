import datetime


def main():
  name = input('Whats your name? ')
  age = input('Whats your age? ')
  output = "Your name is {}, age {}, you will finish 100 in {}".format(
      name, age, int(datetime.date.today().strftime("%Y")) - int(age) + 100)
  print(output)
  count = input('How many times?')
  for i in range(int(count)):
    print(output)


if __name__ == '__main__':
  main()
