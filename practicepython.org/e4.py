''' https://www.practicepython.org/
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

def divisors(number):
  out = []
  for i in range(2, number):
    if number % i == 0:
      out.append(i)
  return(out)

def main():
  number = int(input('Whats your number? '))
  print("divisors of {} are:".format(number))
  print(divisors(number))

if __name__ == '__main__':
  main()
