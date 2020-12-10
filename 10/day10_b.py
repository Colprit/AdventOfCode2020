with open('day10_input.txt') as f:
  data = f.readlines()

adaptors = [int(a) for a in data]
adaptors.sort()

adap_prev = [0, *[-a for a in adaptors]]
adap_next = [*adaptors, max(adaptors)+3]

diffs = list(map(sum, zip(adap_prev, adap_next))) 

total_ways = 1
one_seqs = {0:1, 1:1, 2:2, 3:4, 4:7}
i = 0
for d in diffs:
  if d == 1:
    i += 1
  else:
    total_ways *= one_seqs[i]
    i = 0

print(total_ways)