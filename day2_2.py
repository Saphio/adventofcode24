## DAY 2: PART 1

## greedily, we can remove the first instance where the report is unsafe
## and check if it now passes the test. otherwise, the report will never
## be safe no matter what is removed.

## the "first instance" can manifest itself in different forms - since the 
## input is small, we can just check all three forms each time. that means
## removing arr[0], arr[i - 1], and arr[i] independently, where 
# ## arr[i] - arr[i - 1] makes the report unsafe.

def safe (report, flag = True):
    if (len(report) < 2): return True
    increasing = (report[1] - report[0]) > 0
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if ((1 > diff or 3 < diff) or
            (increasing and report[i] < report[i - 1]) or
            (not increasing and report[i] > report[i - 1])):
            if (flag):
              report0 = list(report)
              reportB = list(report)
              report.pop(i)
              report0.pop(0)
              reportB.pop(i - 1)
              return safe(report, False) or safe(report0, False) or safe(reportB, False)
            else:
                return False
           
    return True

f = open("./AdventOfCode/day2.txt", "r")

reports = []
line = f.readline()
count = 0
while (line != ""):
    report = [int(i) for i in line.split()]
    if (safe(report)):
        count += 1
    line = f.readline()
    
f.close()

print(count)
