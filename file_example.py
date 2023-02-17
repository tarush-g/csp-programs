import time

fhand = open("mbox-short.txt")
count=0
for line in fhand:
    line = line.strip()
    line= line.split()
    for word in line:
        if word.lower() == 'for':
            count+=1
print(count)
