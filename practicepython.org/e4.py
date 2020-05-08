# https://www.practicepython.org/

def main():

  number = int(input('Whats your number? '))
  print("divisors of {} are:".format(number))
  for i in range(2, number):
    if number % i == 0:
      print(i)


if __name__ == '__main__':
  main()
