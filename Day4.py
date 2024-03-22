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

# Part 2

# Idea: We need to find areas of intersecting circles for each pair, and keep track of the max area
# Process for calculating area of intersecting circles adapted from https://www.geeksforgeeks.org/area-of-intersection-of-two-circles/
max_area: int = 0

for i, router1 in enumerate(routers):
  for router2 in routers[i + 1:]:
    distance = math.dist(router1[0:2], router2[0:2])
    radius1 = router1[2]
    radius2 = router2[2]

    # If distance is greater than then area of intersection is 0, because they don't intersect
    if distance > radius1 + radius2:
      continue
    # If distance is less than difference of radii, then one circle envelops the other
    if distance <= (radius1 - radius2) and radius1 >= radius2:
        area = math.floor(math.pi * (radius2 ** 2))
    elif distance <= (radius2 - radius1) and radius2 >= radius1:
        area = math.floor(math.pi * (radius1 ** 2))
    else:
      alpha = math.acos(((radius1 ** 2) + (distance ** 2) - (radius2 ** 2)) / (2 * radius1 * distance)) * 2
      beta  = math.acos(((radius2 ** 2) + (distance ** 2) - (radius1 ** 2)) / (2 * radius2 * distance)) * 2

      a1 = (0.5 * beta * (radius2 ** 2)) - (0.5 * (radius2 ** 2) * math.sin(beta))
      a2 = (0.5 * alpha * (radius1 ** 2)) - (0.5 * (radius1 ** 2) * math.sin(alpha))
      area = math.floor(a1 + a2)

    if area > max_area:
      max_area = area

print(max_area)
