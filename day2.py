## DAY 2: PART 1

def safe (report):
    if (len(report) < 2): return True
    if (report[1] - report[0] < 0): ## decreasing
        for i in range(1, len(report)):
            if (-3 <= report[i] - report[i - 1] <= -1):
                continue
            else:
                return False
    else: ## increasing
        for i in range(1, len(report)): 
            if (3 >= report[i] - report[i - 1] >= 1):
                continue
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
