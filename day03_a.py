with open('day03_input.txt') as f:
  slope = f.read()

slope = slope.replace(".", '0')
slope = slope.replace("#", '1')
slope = slope.split('\n')
slope = [list(lat) for lat in slope]
slope = [[int(pos) for pos in lat] for lat in slope]

# width of the repeating pattern
wid = len(slope[0])

# movement
movX = 3
movY = 1

posX = 0
posY = 0

trees = 0
while posY < len(slope):
  trees += slope[posY][posX%wid]
  posX += movX
  posY += movY

print(trees)