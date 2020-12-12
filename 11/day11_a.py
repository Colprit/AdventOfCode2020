with open('day11_input.txt') as f:
  layout = f.read()

layout = layout.split('\n')
Y = len(layout)
X = len(layout[0])

def adj_occ(layout, y, x):
  occ = 0
  adj_pos = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,-1],
    [1,0],
    [1,1]
  ]
  for adj in adj_pos:
    if 0 <= y+adj[0] < Y:
      if 0 <= x+adj[1] < X: 
        if layout[y+adj[0]][x+adj[1]] == '#':
          occ += 1
  return occ

def new_state(layout, y, x):
  curr = layout[y][x]
  if curr == 'L':
    if adj_occ(layout, y, x) == 0:
      return '#'
  elif curr == '#':
    if adj_occ(layout, y, x) >= 4:
      return 'L'
  return curr

def print_lay(layout):
  for row in layout:
    print(row)

layA = layout.copy()
while True:
  layB = [''.join([new_state(layA,y,x) for x in range(X)]) for y in range(Y)]
  if layA == layB:
    break
  layA = layB.copy()

total_occ = sum(row.count('#') for row in layA)
print(total_occ)
