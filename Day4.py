# Part 1

import re
import math

# Idea:
# Each router is a point with a circle of radius 'range' around it
# We're looking for routers with intersecting ranges, in other words looking for intersecting circles
# Since circles are the same no matter how your rotate them, manhole principle, then any intersections at an edge are the same
# The furthest two intersecting circles can be is to be intersecting on an edge.
# Since all intersections at an edge are the same, we can draw a line with a length of (range1 + range2) between the centers of the circles, the routers
# Get all points (routers) with their radii (ranges). If the distance between any two points is less than or equal to their radii added together, they are a pair

pairs: int = 0
routers: list[tuple[int]] = []

# RegEx to get the number from the txt files
retrieve_numbers = re.compile(r'x=(\d+), y=(\d+) with reach=(\d+)')

with open("Day4Input.txt", "r", encoding = "utf-8") as f:
  for line in f.readlines():
    # routers is an list of tuples of int. The elements of each router are x, y, and reach respectively
    router = re.findall(retrieve_numbers, line)[0]
    router = tuple(int(i) for i in router)
    routers.append(router)

router1: tuple[int]
router2: tuple[int]

for i, router1 in enumerate(routers):
  # for every router, we look at every other router that has not been looked at yet, to avoid double-counting
  for router2 in routers[i + 1:]:
    if math.dist(router1[0:2], router2[0:2]) <= (router1[2] + router2[2]):
      pairs += 1
print(pairs)
