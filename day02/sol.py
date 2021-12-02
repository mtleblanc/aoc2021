import sys

x = 0
y = 0
aim = 0
for line in sys.stdin:
  cmd, val = line.split()
  if cmd == 'forward':
      x += int(val)
      y += int(val) * aim
  elif cmd == 'up':
      aim -= int(val)
  elif cmd == 'down':
      aim += int(val)
  else:
      raise Exception()

print(x*y)
