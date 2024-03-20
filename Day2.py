# Part 1
# ORIGINAL SOLUTION
# room = open("Day2Input.txt", "r", encoding = "utf-8")
# num_m2 = 0

# for line in room:
#   left = line.split(' ')[0]
#   num_m2 += left.count('.')

# print(num_m2)

# Code chunk below provided by Pillow to fix origin input txt file, which incorrectly had a duplicate
grid = []
with open("Day2Input.txt", "r") as f:
  for line in f.readlines():
    # left = line.split(' ')[0] # This was used when the input file was incorrect
    grid.append([c for c in line])

num_m2 = 0
for line in grid:
  num_m2 += line.count('.')

print(num_m2)

# Part 2 First Approach Attempt

num_places = 0
rows = len(grid)
cols = len(grid[0])

# For every row in the grid, excluding those where we wouldn't have enough space to put a 15x15 box if they were the top row
for row in range(rows - 14):
  # current_empty_cols keeps track of how many empty columns we have
  current_empty_cols = 0
  occupied = False
  # For every element in the current row
  for col in range(cols):
    # Check elements downward vertically until we have 15 elements or we reach an occupied '#' space
    for x in range(15):
      # If we reach an occupied '#' space, stop going down and move right to the next element
      if grid[row + x][col] != '.':
        # Reset current_empty_cols since an occupied space is in the way of making a box
        occupied = True
        break
    # If we go down for 15 elements without encountering an occupied space, increment current_empty_cols by 1
    if occupied:
       current_empty_cols = 0
       occupied = False
    else:
       current_empty_cols += 1
    # If we have 15 empty columns, we can place a hypothetical box there
    if current_empty_cols >= 15:
      num_places += 1
      # We decrement current_empty_cols by 1 to account for overlapping boxes 1 space apart
      current_empty_cols -= 1

print(num_places)

# Part 2 Second Approach Attempt
num_places = 0
def fits_box(row, col):
  for x in range(15):
    for y in range(15):
      if grid[row + x][col + y] != '.':
        return False
  return True

for row in range(rows - 14):
  for col in range(cols - 14):
    if fits_box(row, col):
      num_places += 1
print(num_places)
