''' https://www.practicepython.org/ 
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter 
the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers 
where the next number in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def fibonnaci(number):
  if number == 1:
    list = [1]
  else:
    list = [1, 1]
    for i in range(number-2):
      #list.append(list[i]+list[i+1])
      list.append(list[-2]+list[-1])
  return(list)

def main():
  number = int(input("Number for Fibonnaci: "))
  print(fibonnaci(number))
  
if __name__ == "__main__":
  main()