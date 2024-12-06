def getline():
  if (d % 2 == 1):
    line = grid[x]
    line = "".join(line)
  else:
    line = [grid[i][y] for i in range(len(grid))]
    line = "".join(line)
  return line

f = open("day6.txt", "r")
grid = []
d = 0 ## 0 = up, 1 = right, 2 = down, 3 = left

## make grid, find initial position
line = f.readline()
foundCoords = False
x = 0
y = 0
while (line != ""):
  if ("^" in line):
    foundCoords = True
    y = line.index("^")
  grid.append(list(line.strip()))
  if (not foundCoords):
    x += 1
  line = f.readline()

## step
a = 0
while (True):
  # print(x, y)
  turned = False
  line = getline()
  if (d == 0):
    n = -1
    for i in range(x - 1, -1, -1):
      if (line[i] == "#"):
        n = i
        break
    print("found:", x, y, n)
    for i in range(n + 1, x + 1):
      grid[i][y] = "X"
    x = n + 1
    d += 1
    turned = True
    line = getline()
  # for l in grid: print("".join(l))
  if (d == 1):
    # print(line)
    n = line.find("#", y + 1)
    if (n == -1):
      n = len(grid[0])
    # print('\n', line)
    for i in range(y, n):
      grid[x][i] = "X"
    if (turned and n <= y):
      break ## failed
    # print(n, y)
    y = n - 1
    d += 1
    turned = True
    line = getline()
  if (d == 2):
    n = line.find("#", x + 1)
    if (n == -1):
      n = len(grid)
    # print(x, y, n)
    for i in range(x, n):
      grid[i][y] = "X"
    if (turned and n <= x):
      break ## failed
    x = n - 1
    d += 1
    turned = True
    # print('after', x, y, d)
    line = getline()
  if (d == 3):
    n = -1
    for i in range(y - 1, -1, -1):
      if (line[i] == "#"):
        n = i
        break
    # print(x, y, n)
    # for line in grid: print("".join(line))
    for i in range(n + 1, y):
      grid[x][i] = "X"
    if (turned and n + 1 > y):
      break
    y = n + 1
    d = 0
    turned = True
    line = getline()
  ## print(x, y, d, a)
  a += 1
  if (a > 2):
    break

## for l in grid:
  ## print("".join(l))

count = 0
for line in grid:
  l = "".join(line)
  count += l.count("X")

print(count)
