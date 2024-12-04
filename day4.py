## DAY 4: PART 1

def matches (word):
  if (word == "XMAS" or word == "SAMX"):
    return True
  return False

f = open("AdventOfCode/day4.txt", "r")
grid = f.readlines()
f.close()

total = 0
rows = len(grid)

## horizontal
for r in range(rows):
  grid[r] = grid[r].strip()
  line = grid[r]
  total += line.count("XMAS")
  total += line.count("SAMX")

cols = len(grid[0])

## vertical
for c in range(cols):
  for r in range(rows - 3):
    word = grid[r][c] + grid[r + 1][c] + grid[r + 2][c] + grid[r + 3][c]
    if (matches(word)):
      total += 1

## diagonal
for r in range(rows - 3):
  for c in range(cols - 3):
    ## \ diagonal
    word = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] + grid[r + 3][c + 3]
    if (matches(word)):
      total += 1
    ## / diagonal
    word = grid[r + 3][c] + grid[r + 2][c + 1] + grid[r + 1][c + 2] + grid[r][c + 3]
    if (matches(word)):
      total += 1

print(total)
