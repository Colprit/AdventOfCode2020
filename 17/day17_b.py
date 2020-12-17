with open('day17_input.txt') as f:
    data = f.read().split('\n')

start = {}

for x in range(len(data)):
    for y in range(len(data[0])):
        if data[x][y] == '#':
            start.update({ (x,y,0,0) : 1 })

def nhbrs(x,y,z,w):
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                for l in range(w-1,w+2):
                    if not (i==x and j==y and k==z and l==w):
                        yield (i,j,k,l)

def max_min(config):
    for dim in range(4):
        vals = [key[dim] for key in config.keys()]
        yield min(vals)-1, max(vals)+2

def count_nhbrs(config, x, y, z, w):
    total = 0
    for nhbr in nhbrs(x,y,z,w):
        total += config.get(nhbr, 0)
        if total > 3:
            break
    return total

config = start.copy()

steps = 6

for step in range(steps):
    next_config = config.copy()
    minmaxX, minmaxY, minmaxZ, minmaxW = max_min(config)
    for x in range(*minmaxX):
        for y in range(*minmaxY):
            for z in range(*minmaxZ):
                for w in range(*minmaxW):
                    if config.get((x,y,z,w), 0):
                        if not 2 <= count_nhbrs(config, x, y, z, w) <= 3:
                            next_config.pop((x,y,z,w))
                    else:
                        if count_nhbrs(config, x, y, z, w) == 3:
                            next_config.update({ (x,y,z,w) : 1 })
    config = next_config.copy()

print(len(config))
