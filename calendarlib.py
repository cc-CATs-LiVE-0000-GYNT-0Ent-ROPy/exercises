from collections import OrderedDict


def boundries2mettings(bouhours):
  bound2meetslotss = [['0:00', bouhours[0]], [bouhours[1], '23:00']]
  print(bound2meetslotss)
  return bound2meetslotss

# returns occupied slots in whole day
# change meetings hour into dictionary of 30min slots


def meetings2slots(calhours, boundries):
  meetings = {}
  for i in range(len(calhours)):
    meetings.update(meeting2slots(calhours[i]))
  boundmeet = boundries2mettings(boundries)
  for i in range(len(boundmeet)):
    meetings.update(meeting2slots(boundmeet[i]))

  orderedprint(meetings)
  return meetings

# change meeting hour into dictionary of 30min slots
'''
8:00 9:00
8:30 9:00
8:00 9:30
8:30 9:30

'''

def meeting2slots(hour):  # change meetings hour into dictionary of 30min slots
  #print("meeting - start {}, stop {}".format(int(hour[0][:-3]), int(hour[1][:-3])))
  meetslots = {'%s:%s' % (h, m)
               for h in ([int(hour[0][:-3])] + list(range(int(hour[0][:-3]) + 1, int(hour[1][:-3]) + 1)))
               for m in ('00', '30')
               }
  return dict.fromkeys(meetslots, 0)


def orderedprint(dict):
  print(OrderedDict(sorted(dict.items())))
