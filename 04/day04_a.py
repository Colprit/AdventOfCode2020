with open('day04_input.txt') as f:
  pps = f.read()

pps = pps.replace('\n\n', '£').replace('\n', ' ')
pps = pps.split('£')

req = [
  'byr',
  'iyr',
  'eyr',
  'hgt',
  'hcl',
  'ecl',
  'pid'
]

invalid = 0

for pp in pps:
  for field in req:
    if field not in pp:
      invalid += 1
      break

print(len(pps) - invalid)
