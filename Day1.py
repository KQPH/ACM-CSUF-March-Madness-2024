import re
services = open('Day1.txt', 'r', encoding = "utf-8")

num_boot = 0
num_lines = 0

for line in services:
  if re.search("\[STOP\]", line) != None:
    num_boot += 1

  num_lines += 1

print(num_boot)
print(num_boot + num_lines)
