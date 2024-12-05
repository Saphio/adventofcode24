## DAY 5: PART 2

## check validity of order; returns true if correct
def checkOrder (order):
  for i in range(len(order)):
    cur = order[i]
    for n in edges[cur]:
      if (n in order[:i]):
        return False
  return True

## re-orders the order to topological ordering
def reOrder (order):
  i = 0
  while (i < len(order)):
    cur = order[i]
    for n in edges[cur]:
      if (n in order[:i]):
        ## shift back
        j = order.index(n)
        order = order[:j] + order[j + 1:i + 1] + [n] + order[i + 1:]
        i = -1
        break
    i += 1
  return order

f = open("day5.txt", "r")
edges = [[] for _ in range(101)]
indegree = [0 for _ in range(101)]

line = f.readline().strip()
while (line != ""):
  a, b = map(int, line.split("|"))
  edges[a].append(b)
  indegree[b] += 1
  line = f.readline().strip()

line = f.readline().strip()
total = 0
while (line != ""):
  order = list(map(int, line.split(",")))
  if (not checkOrder(order)):
    order = reOrder(order)
    total += order[int(len(order)/2)]
  line = f.readline().strip()

print(total)
