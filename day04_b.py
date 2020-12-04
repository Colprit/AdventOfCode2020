import re

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

def valYr(val, minYr, maxYr):
  if len(val) == 4:
      if minYr <= int(val) <= maxYr:
        return True
  return False

def valHgt(val):
  if 4 <= len(val) <= 5:
    numb = int(val[:-2])
    unit = val[-2:]
    if unit == 'cm':
      if 150 <= numb <= 193:
        return True
    elif unit == 'in':
      if 59 <= numb <= 76:
        return True
  return False

def valField(field):
  name, val = field.split(':')
  # appropriate check for each field type
  if name == 'byr':
    return valYr(val, 1920, 2002)
  elif name == 'iyr':
    return valYr(val, 2010, 2020)
  elif name == 'eyr':
    return valYr(val, 2020, 2030)
  elif name == 'hgt':
    return valHgt(val)
  elif name == 'hcl':
    return len(val) == 7 and re.search(r'#[0-9a-f]{6}', val)
  elif name == 'ecl':
    return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  elif name == 'pid':
    return len(val) == 9 and re.search(r'[0-9]{9}', val)
  elif name == 'cid':
    return True
  else:
    return False

def valPP(pp):
  # check for all req fields
  for field in req:
    if field not in pp:
      return False
  # check fields are valid
  fields = pp.split(' ')
  print(fields)
  for f in fields:
    if not valField(f):
      return False
  # all fields valid so pp valid
  print("valid")
  return True

valid = 0
for pp in pps:
  if valPP(pp):
    valid += 1

print(valid)
