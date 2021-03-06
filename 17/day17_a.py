with open('day17_input.txt') as f:
    data = f.read().split('\n')

start = {}

for x in range(len(data)):
    for y in range(len(data[0])):
        if data[x][y] == '#':
            start.update({ (x,y,0) : 1 })

print(start)

def nhbrs(x,y,z):
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                if not (i==x and j==y and k==z):
                    yield (i,j,k)

def max_min(config):
    for dim in range(3):
        vals = [key[dim] for key in config.keys()]
        yield min(vals)-1, max(vals)+2

def count_nhbrs(config, x, y, z):
    total = 0
    for nhbr in nhbrs(x,y,z):
        total += config.get(nhbr, 0)
        if total > 3:
            break
    return total

config = start.copy()

steps = 6

for step in range(steps):
    next_config = config.copy()
    minmaxX, minmaxY, minmaxZ = max_min(config)
    for x in range(*minmaxX):
        for y in range(*minmaxY):
            for z in range(*minmaxZ):
                if config.get((x,y,z), 0):
                    if not 2 <= count_nhbrs(config, x, y, z) <= 3:
                        next_config.pop((x,y,z))
                else:
                    if count_nhbrs(config, x, y, z) == 3:
                        next_config.update({ (x,y,z) : 1 })
    config = next_config.copy()

print(len(config))
