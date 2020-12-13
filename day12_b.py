with open('day12_input.txt') as f:
  data = f.read()

instrs = data.split('\n')[:-1]

x = 0
y = 0
way_x = 10
way_y = 1

dir_dic = {
  'N': [ 0, 1],
  'E': [ 1, 0],
  'S': [ 0,-1],
  'W': [-1, 0]
}

ang_dic = {
    0: 'E',
   90: 'N',
  180: 'W',
  270: 'S'
}

def rot(x,y,ang):
    N = int(((ang)%360)/90)
    X,Y = x,y
    for i in range(N):
        X,Y = -Y, X
    return X, Y

for instr in instrs:
  i = instr[0]
  n = int(instr[1:])

  if i == 'F':
    x += way_x * n
    y += way_y * n
  elif i == 'L' or i == 'R':
    if i == 'R':
        n *= -1
    way_x, way_y = rot(way_x, way_y, n)
  else:
    mov = dir_dic[i]
    way_x += mov[0] * n
    way_y += mov[1] * n

print(abs(x)+abs(y))

