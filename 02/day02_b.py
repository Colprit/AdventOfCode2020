with open('day02_input.txt') as f:
  data = f.read().replace(":", "")

pwords = data.split("\n")
pwords.remove('')

valid = 0

for pword in pwords:
  pos, let, word = pword.split()
  posLets = [word[int(x)-1] for x in pos.split("-")]
  if posLets.count(let) == 1:
    valid += 1

print(valid)