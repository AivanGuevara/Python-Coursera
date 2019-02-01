fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        splittedLine = line.split()
        print(splittedLine[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")

name = input("Enter file:")
hourCount = dict()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    strippedLine = line.rstrip()
    if strippedLine.startswith('From') and not strippedLine.startswith('From:'):
        splittedLine = strippedLine.split()
        hourMinutesSeconds = splittedLine[5]
        hourSplitted = hourMinutesSeconds.split(":")
        hourCount[hourSplitted[0]] = hourCount.get(hourSplitted[0],0) + 1
print(sorted(hourCount))        
            