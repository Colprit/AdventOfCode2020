with open('day07_input.txt') as f:
  data = f.read()

rules = data.split('.\n')

bags_contain = {}

for rule in rules:
  bag, content = rule.split(' contain ')
  # remove words ' bags'
  bag_colour = bag[:-5]
  # split into list of bags inside
  content = content.split(', ')
  in_colours = {}
  for b in content:
    if b != 'no other bags':
      words = b.split()
      num = int(words[0])
      col = ' '.join(words[1:-1])
      in_colours.update({col:num})
  bags_contain.update({bag_colour: in_colours})

def total_within(bag_col):
  print(bag_col)
  content = bags_contain.get(bag_col, {})
  if content == {}:
    return 0
  else:
    return sum([
      content[col] * (1 + total_within(col)) for col in content
    ])

shiny_gold_contains = total_within('shiny gold')

print(shiny_gold_contains)