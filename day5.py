## DAY 5: PART 1

def checkOrder (order):
  for i in range(len(order)):
    cur = order[i]
    for n in edges[cur]:
      if (n in order[:i]):
        return False
  return True

f = open("day5.txt", "r")
edges = [[] for _ in range(101)]

line = f.readline().strip()
while (line != ""):
  a, b = map(int, line.split("|"))
  edges[a].append(b)
  line = f.readline().strip()

line = f.readline().strip()
total = 0
while (line != ""):
  order = list(map(int, line.split(",")))
  if (checkOrder(order)):
    total += order[int(len(order)/2)]
  line = f.readline().strip()

print(total)
