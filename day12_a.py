with open('day12_input.txt') as f:
  data = f.read()

instrs = data.split('\n')[:-1]

x = 0
y = 0
dir = 0

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

for instr in instrs:
  i = instr[0]
  n = int(instr[1:])

  if i == 'F':
    mov = dir_dic[ang_dic[dir]]
    x += mov[0] * n
    y += mov[1] * n
  elif i == 'L':
    dir = (dir+n)%360
  elif i == 'R':
    dir = (dir-n)%360
  else:
    mov = dir_dic[i]
    x += mov[0] * n
    y += mov[1] * n

print(x,y)
print(x+y)

