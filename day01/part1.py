import sys

prevVal = None
increases = 0
for line in sys.stdin:
    curVal = int(line)
    if prevVal != None and curVal > prevVal:
        increases += 1
    prevVal = curVal

print(increases)
