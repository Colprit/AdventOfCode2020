with open('day13_input.txt') as f:
    data  = f.read()

earliest, buses = data.split()
earliest = int(earliest)
buses = buses.replace('x,', '').split(',')
buses = [int(b) for b in buses]

time_until = [-earliest % bus for bus in buses]
wait = min(time_until)
bus_to_take = buses[time_until.index(wait)]

print(bus_to_take * wait)