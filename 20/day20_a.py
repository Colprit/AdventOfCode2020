with open('day20_input.txt') as f:
    tiles_data = f.read().split('\n\n')[:-1]

tiles = {}

for tile_data in tiles_data:
    ref, tile = tile_data.split(':\n')
    tile = tile.replace('.', '0').replace('#','1')
    tiles.update({int(ref[5:]) : tile.split('\n')})


def rot90(tile, n=1):
    if n == 0:
        return tile
    else:
        I = range(len(tile))
        J = range(len(tile[0]))
        new_tile = [''.join(tile[i][-j-1] for i in I) for j in J]
        return rot90(new_tile, n-1)

def flip(tile, axis):
    if axis == 'x':
        return tile[-1::-1]
    elif axis == 'y':
        return [row[-1::-1] for row in tile]
    else:
        return 'error'

def borders_of(tile):
    codes = []
    for i in range(4):
        border = rot90(tile, i)[0]
        codes.append( min(int(border, 2), int(border[-1::-1], 2)) )
    return codes

borders = {}
borders_to_tiles = {}

for ref, tile in tiles.items():
    bords = borders_of(tile)
    borders.update({ ref : bords })
    for border in bords:
        x = borders_to_tiles.get(border, [])
        if not ref in x:
            borders_to_tiles.update({border: x+[ref]})

outer_borders = {}

for refs in borders_to_tiles.values():
    if len(refs) == 1:
        ref = refs[0]
        y = outer_borders.get(ref,0)
        outer_borders.update({ ref : y + 1 })

corners = []

for ref, outer in outer_borders.items():
    if outer == 2:
        corners.append(ref)

total = 1
for c in corners:
    total *= c

print(total)

