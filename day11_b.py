with open('day11_input.txt') as f:
  layout = f.read()

layout = layout.split('\n')
Y = len(layout)
X = len(layout[0])

def adj_occ_full(layout, y, x):
  occ = 0
  adj_dir = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,-1],
    [1,0],
    [1,1]
  ]
  for dir in adj_dir:
    curr_y = y + dir[0]
    curr_x = x + dir[1]
    while 0 <= curr_y < Y and 0 <= curr_x < X:
      if layout[curr_y][curr_x] == '#':
        occ += 1
        if occ == 5:
          return 5
        break
      elif layout[curr_y][curr_x] == 'L':
        break
      curr_y += dir[0]
      curr_x += dir[1]
  return occ

def adj_occ_empty(layout, y, x):
  adj_dir = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,-1],
    [1,0],
    [1,1]
  ]
  for dir in adj_dir:
    curr_y = y + dir[0]
    curr_x = x + dir[1]
    while 0 <= curr_y < Y and 0 <= curr_x < X:
      if layout[curr_y][curr_x] == '#':
        return 1
      elif layout[curr_y][curr_x] == 'L':
        break
      curr_y += dir[0]
      curr_x += dir[1]
  return 0

def new_state(layout, y, x):
  curr = layout[y][x]
  if curr == 'L':
    if adj_occ_empty(layout, y, x) == 0:
      return '#'
  elif curr == '#':
    if adj_occ_full(layout, y, x) >= 5:
      return 'L'
  return curr

layA = layout.copy()
while True:
  layB = [''.join([new_state(layA,y,x) for x in range(X)]) for y in range(Y)]
  if layA == layB:
    break
  layA = layB.copy()

total_occ = sum(row.count('#') for row in layA)
print(total_occ)
