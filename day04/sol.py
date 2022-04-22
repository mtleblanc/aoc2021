#!/usr/bin/python3

import sys
import itertools

f = open("input", "r")

nums = [int(i) for i in f.__next__().split(',')]
f.__next__()
cnt = 0
boards = []
newboard = []
for l in f:
  if(cnt < 5):
    newboard.append([int(i) for i in l.strip().split(' ') if len(i) > 0])
    cnt += 1
  else:
      cnt = 0
      boards.append(newboard)
      newboard = []
boards.append(newboard)

winNum = None

nextBoards = [b for b in boards]
for d in nums:
    newestBoards = []
    if len(nextBoards) == 0:
        break
    for b in nextBoards:
        for r in b:
            for i,c in enumerate(r):
                if c == d:
                    r[i] = -1
    for j,b in enumerate(nextBoards):
        boardWins = False
        for r in b:
            if sum(r) == -5:
                boardWins = True
                winner = b
                winNum = d
        for c in range(5):
            if sum((r[c] for r in b)) == -5:
                boardWins = True
                winner = b
                winNum = d
        if not boardWins:
            newestBoards.append(b)
    nextBoards = [b for b in newestBoards]

for r in winner:
    for i,c in enumerate(r):
        if c == -1:
            r[i] = 0

print(winNum * sum([sum(r) for r in winner]))    
