#!/usr/bin/python3

import sys
import itertools

f = open("input", "r")
fish = []
for l in f:
    fish.extend((int(i) for i in l.split(',')))

# fish = [3,4,3,1,2]

sizes = []
sizes.append(len(fish))

while(len(sizes) < 9):
    newfish = []
    for i,d in enumerate(fish):
        if d == 0:
            d = 7
            newfish.append(8)
        fish[i] = d-1
    fish.extend(newfish)
    sizes.append(len(fish))

while(len(sizes) <=256):
    index = len(sizes)
    sizes.append(sizes[index-7] + sizes[index-9])

for i,j in enumerate(sizes):
    print(f'{i:2}: {j}')
