# Part 1

import re

logs: list[tuple] = []

# RegEx to get the log from the txt file
retrieve_log = re.compile(r'(\d+): (\w+) (<-|->) (\w+)')

with open("Day5Input.txt", "r", encoding = "utf-8") as f:
  for line in f.readlines():
    # log is an list of tuples. The elements of each log are time, person name, enter/exit, and building name respectively
    log: tuple = re.findall(retrieve_log, line)[0]
    fixed_log = (int(log[0]), log[1], log[2], log[3])
    logs.append(fixed_log)

logs.sort()
# Idea: If everyone starts outside the buildings, in other words if everyone must enter a building
# before they can exit it, then this is similar to a parantheses-checking problem, except arrows don't have
# to maintain a corresponding order, so a stack won't work
enter_list: list = []

for log in logs:
  direction = log[2]
  # If we log an entry, add it to enter_list
  if direction == "->":
    enter_list.append(log)
  # If we log an exit, check if there is a corresponding entry
  elif direction == "<-":
    # If the person's name comes up in the enter_list and they entered the right building, remove them from enter_list
    for entry in enter_list:
      if log[1] in entry[1] and log[3] in entry[3]:
        enter_list.remove(entry)
        break
# The only log remaining in enter_list will be suspicious
print(enter_list)

# Part 2

import datetime

sus_date = datetime.datetime.fromtimestamp(enter_list[0][0], tz=datetime.timezone(datetime.timedelta(hours=-8))).date()
print(sus_date)

suspects: set = set()
sus_entries: int = 0

for log in logs:
  log_date = datetime.datetime.fromtimestamp(log[0], tz=datetime.timezone(datetime.timedelta(hours=-8))).date()
  # If it is the same day
  if log_date == sus_date:
    # If there is an entry on that day, add the person to suspects and increment sus_entries
    if log[2] == "->":
      # Since sets are unique, add will be ignored if they are already in the set
      suspects.add(log[1])
      sus_entries += 1

print(suspects)
print(len(suspects))
print(sus_entries)
print(len(suspects) * sus_entries)
