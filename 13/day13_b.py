with open('day13_input.txt') as f:
    data  = f.read()

buses = data.split()[1]
all_buses = buses.split(',')

# (bus number, time offset)
buses = [(int(b), all_buses.index(b)) for b in all_buses if b != 'x']

t = 0
mod = 1
for (id, offset) in buses:
    while t % id != -offset % id:
        t += mod
    mod *= id

print(t)
