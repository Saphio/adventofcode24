## DAY 3: PART 1

def solve(line):
  status = 0 ## 0 = no command, 1 = first num, 2 = second num, 3 = done
  command = ""
  a = ""
  b = ""
  i = 0
  total = 0
  while (i < len(line)):
    ## building up command
    if (status == 0):
      command += line[i]
      if (command != "m" and command != "mu" and command != "mul" and command != "mul("):
        command = line[i]
      if (command == "mul("):
        command = ""
        status = 1
    ## first number
    elif (status == 1):
      if (line[i] == "," and a != ""):
        status = 2
      else:
        a += line[i]
        if (not a.isnumeric()):
          status = 0
          a = ""
    ## second number
    elif (status == 2):
      if (line[i] == ")" and b != ""):
        status = 3
      else:
        b += line[i]
        if (not b.isnumeric()):
          status = 0
          a = ""
          b = ""
    ## execute command
    if (status == 3):
      total += int(a) * int(b)
      a = ""
      b = ""
      status = 0

    i += 1

  return total


f = open("AdventOfCode/day3.txt", "r")
line = f.readline()
s = 0

while (line != ""):
  s += solve(line)
  line = f.readline()

print(s)
