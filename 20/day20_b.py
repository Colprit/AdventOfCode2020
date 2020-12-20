# with open('day20_eg.txt') as f:
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

def get_border(ref, side):
    global borders
    sides = {
        'top': 0,
        'right': 1,
        'bottom': 2,
        'left': 3
    }
    return borders[ref][sides[side]]


# ref : [ border codes ]
borders = {}
# border code : [ refs ]
borders_to_tiles = {}

for ref, tile in tiles.items():
    bords = borders_of(tile)
    borders.update({ ref : bords })
    for border in bords:
        x = borders_to_tiles.get(border, [])
        if not ref in x:
            borders_to_tiles.update({border: x+[ref]})

# ref : outer edges
edges = {}
for border, refs in borders_to_tiles.items():
    if len(refs) == 1:
        ref = refs[0]
        y = edges.get(ref, [])
        edges.update({ ref : y+[border] })


# ref : outer edges
corners = {}
for ref, edge_borders in edges.items():
    if len(edge_borders) == 2:
        corners.update({ ref : edge_borders })


def orient(ref, top_b, left_b):
    global tiles, borders
    
    tile = tiles[ref]
    bords = borders[ref]

    index_top = bords.index(top_b)
    index_left = bords.index(left_b)

    tile = rot90(tile, index_top)
    if (index_top+1)%4 == index_left:
        tile = flip(tile, 'y')
    
    tiles[ref] = tile
    borders[ref] = borders_of(tile)
    
    return tile



start_ref = list(corners.keys())[0]

picture = [[start_ref]]

orient(start_ref, *corners[start_ref])

# determine top row
x = 0
y = 0

fin_row = False

while not fin_row:

    prev = picture[x][y]

    to_match = get_border(prev, 'right')

    next = borders_to_tiles[to_match]
    next.remove(prev)
    next = next[0]

    if not next in corners:
        edge = edges[next][0]
    else:
        bords = borders[next]
        k = bords.index(to_match)
        if bords[(k+1)%4] in corners[next]:
            edge = bords[(k+1)%4]
        else:
            edge = bords[(k-1)%4]
    
    orient(next, edge, to_match)
    picture[x].append(next)
    
    if next in corners:
        fin_row = True
    
    y += 1


print('first row')
print(picture)

# determine left column
x = 0
y = 0

fin_col = False

while not fin_col:

    prev = picture[x][y]

    to_match = get_border(prev, 'bottom')

    next = borders_to_tiles[to_match]
    next.remove(prev)
    next = next[0]

    if not next in corners:
        edge = edges[next][0]
    else:
        bords = borders[next]
        k = bords.index(to_match)
        if bords[(k+1)%4] in corners[next]:
            edge = bords[(k+1)%4]
        else:
            edge = bords[(k-1)%4]
    
    orient(next, to_match, edge)
    picture.append([next])
    
    if next in corners:
        fin_col = True
    
    x += 1

print('first row and col')
print(picture)

# determine rest of picture
x = 1
y = 0

fin_pic = False

for x in range(1,len(picture)):

    for y in range(len(picture[0])-1):

        prev = picture[x][y]

        to_match = get_border(prev, 'right')

        next = borders_to_tiles[to_match]
        next.remove(prev)
        next = next[0]

        # get border from above
        top = get_border(picture[x-1][y+1], 'bottom')
        
        orient(next, top, to_match)
        picture[x].append(next)
        

print('whole picture')
print(picture)

full_picture = [''.join([tiles[ref][0] for ref in row]) for i in range(1,9) for row in picture]

for row in full_picture:
    print(row)
    
# for b,t in borders_to_tiles.items():
#     print(b,t)

# for b,t in edges.items():
#     print(b,t)
