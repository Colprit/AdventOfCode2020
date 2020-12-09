with open('day08_input.txt') as f:
  data = f.read()

instrs = data.split('\n')

instrs = [instr.split() for instr in instrs]
instrs = [[instr[0], int(instr[1]), 0] for instr in instrs]

accum = 0
pos = 0
while True:
  instr = instrs[pos]
  if instr[2]:
    break;
  else:
    instrs[pos][2] += 1
    # apply operation
    op, arg = instr[:-1]
    if op == 'acc':
      accum += arg
      pos += 1
    elif op == 'jmp':
      pos += arg
    elif op == 'nop':
      pos += 1
    else:
      print('error')
      break;

print(accum)