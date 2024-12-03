## DAY 3: PART 2

def solve(line, e):
  status = 0 ## 0 = no command, 1 = first num, 2 = second num, 3 = done
  enabled = e
  command = ""
  a = ""
  b = ""
  i = 0
  total = 0
  while (i < len(line)):

    ## building up command
    if (status == 0):
      command += line[i]
      if (command != "m" and command != "mu" and command != "mul" and command != "mul(" and command != "d" and command != "do" and command != "do(" and command != "do()" and command != "don" and command != "don'" and command != "don't" and command != "don't(" and command != "don't()"):
        command = line[i]
      if (command == "do()"):
        enabled = True
        command = ""
      if (command == "don't()"):
        enabled = False
        command = ""
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
      if (enabled): ## only if enabled
        total += int(a) * int(b)
      a = ""
      b = ""
      status = 0

    i += 1

  return total, enabled


f = open("AdventOfCode/day3.txt", "r")
line = f.readline()
s = 0
e = True

while (line != ""):
  t, e = solve(line, e) ## carry over enabled status to next line
  s += t
  line = f.readline()

print(s)
