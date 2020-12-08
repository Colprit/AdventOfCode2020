with open('day06_input.txt') as f:
  data = f.read()

groups = data.split('\n\n')

total = 0
for group in groups:
  forms = group.replace('\n', '')
  total += len(set(forms))

print(total)