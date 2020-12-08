import math

with open('day03_input.txt') as f:
  slope = f.read()

slope = slope.replace(".", '0')
slope = slope.replace("#", '1')
slope = slope.split('\n')
slope = [list(lat) for lat in slope]
slope = [[int(pos) for pos in lat] for lat in slope]

# slope - list of 0s, 1s
# move - [moveX, moveY]
def countTrees(slope, move):
  # width of the repeating pattern
  wid = len(slope[0])

  posX = 0
  posY = 0

  trees = 0
  while posY < len(slope):
    trees += slope[posY][posX%wid]
    posX += move[0]
    posY += move[1]

  return trees

angles = [
  [1,1],
  [3,1],
  [5,1],
  [7,1],
  [1,2]
]

treeCounts = [countTrees(slope, ang) for ang in angles]

print(math.prod(treeCounts))