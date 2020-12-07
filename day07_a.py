with open('day07_input.txt') as f:
  data = f.read()

rules = data.split('.\n')

bags_contain = {}
bags_that_contain = {}

for rule in rules:
  bag, content = rule.split(' contain ')
  # remove words ' bags'
  bag_colour = bag[:-5]
  # split into list of bags inside
  content = content.split(', ')
  in_colours = []
  for b in content:
    words = b.split()
    col = ' '.join(words[1:-1])
    in_colours.append(col)
    if col in bags_that_contain:
      bags_that_contain[col].append(bag_colour)
    else:
      bags_that_contain[col] = [bag_colour]
  bags_contain.update({bag_colour: in_colours})

contain_shiny_gold = set(bags_that_contain['shiny gold'])
while True:
  that_contain = set().union(*[bags_that_contain.get(c,[]) for c in contain_shiny_gold])
  if that_contain.issubset(contain_shiny_gold):
    break;
  contain_shiny_gold = contain_shiny_gold.union(that_contain)

print(len(contain_shiny_gold))