with open('day10_input.txt') as f:
  data = f.readlines()

adaptors = [int(a) for a in data]

adaptors.sort()

adap_prev = [0, *adaptors]
adap_prev = [-a for a in adap_prev]
adap_next = [*adaptors, max(adaptors)+3]

diffs = list(map(sum, zip(adap_prev, adap_next))) 

print(diffs.count(1) * diffs.count(3))