with open ('day05_input.txt') as f:
  bps = f.read()

bps = bps.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

bps = bps.split('\n')

ids = [int(bp,2) for bp in bps]

m = min(ids)
M = max(ids)

for i in range(m,M):
  if i not in ids:
    print(i)
    break