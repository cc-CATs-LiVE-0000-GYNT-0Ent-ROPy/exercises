# https://www.practicepython.org/
import random

a = [random.randint(1, 99) for i in range(random.randint(1, 44))]
a.sort()
b = [random.randint(1, 99) for i in range(random.randint(1, 44))]
b.sort()
print("a {} ".format(a))
print("b {} ".format(b))

out = []


def main():
  for i in a:
    if i in b:
      if i in out:
        pass
      else:
        out.append(i)
  print("out {} ".format(out))


if __name__ == '__main__':
  main()
