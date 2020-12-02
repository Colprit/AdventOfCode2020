with open('day02_input.txt') as f:
  data = f.read().replace(":", "")

pwords = data.split("\n")
pwords.remove('')

valid = 0

for pword in pwords:
  occ, let, pas = pword.split()
  min,max = [int(x) for x in occ.split("-")]
  if min <= pas.count(let) <= max:
    valid += 1

print(valid)