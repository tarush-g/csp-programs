import time
total = 0
elves = []

file = 'day1data.txt'
fhand = open(file)
for line in fhand:
    line = line.strip()
    if line != '':
        total += int(line)
    else:
        elves.append(total)
        total = 0

elves.sort()    
print(sum(elves[-3:]))
