# Source: https://www.youtube.com/watch?v=3Q_oYDQ2whs
# Google Coding Interview With A College Student by  Clément Mihailescu
# Sample input:
c1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
b1 = ['9:00', '20:00']
c2 = [['10:00', '11:30'], ['12:30', '14:30'],
      ['14:30', '15:00'], ['16:00', '17:00']]
b2 = ['10:00', '18:30']
size = 30
# Sample output: [[11:30, 12:00], [15:00, 16:00], [18:00, 18:30]]
#################################################################
import sys
from calendarlib import orderedprint, meeting2slots, meetings2slots

m0 = ['00:00', '23:00']  # for test purpose
m1 = ['9:00', '10:00']  # for test purpose


def mergedic(x, y):
  shared_items2 = {}
  for k in x:
    if k in y:
      shared_items2.update({k: x[k] + 1})
    else:
      shared_items2.update({k: x[k]})
  orderedprint(shared_items2)
  return shared_items2


# returns common free slots
def printslots(dic):
  slots = {}
  for k in dic:
    if dic[k] == 0:
      slots.update({k: dic[k]})
  orderedprint(slots)
  return slots


def main():
  c0dic = meeting2slots(m0)
  c1dic = meetings2slots(c1, b1)
  c2dic = meetings2slots(c2, b2)

  print("xxxxxxxxxxxxxxx")

  slots = printslots(mergedic(mergedic(c0dic, c1dic), c2dic))
  sys.exit(0)


if __name__ == '__main__':
  main()
