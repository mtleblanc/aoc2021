#!/usr/bin/python3

import sys
import itertools

f = open("input", "r")
pos = []
for l in f:
    pos += [int(x) for x in l.split(',')]

pos.sort()
print(pos)
med = pos[len(pos)//2]
print(sum((abs(x - med) for x in pos)))

mean = sum(pos)//len(pos)
print(mean)

print(sum(((x-mean)*(x-mean)+abs(x-mean) for x in pos))//2)
mean += 1
print(sum(((x-mean)*(x-mean)+abs(x-mean) for x in pos))//2)

