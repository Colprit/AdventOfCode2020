with open('day06_input.txt') as f:
  data = f.read()

groups = data.split('\n\n')

total = 0
for group in groups:
  forms = group.split('\n')
  yesPer = [set(form) for form in forms]
  yesAll = set.intersection(*yesPer)
  total += len(yesAll)

print(total)