from copy import deepcopy

with open('day08_input.txt') as f:
  data = f.read()

instrs = data.split('\n')

instrs = [instr.split() for instr in instrs]

def run_program(instrs):
  program = [[instr[0], int(instr[1]), 0] for instr in instrs]
  accum = 0
  pos = 0
  while True:
    if pos >= len(program):
      break;
    else:
      instr = program[pos]
      if instr[2]:
        break;
      else:
        program[pos][2] += 1
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
  return accum, pos

terminate_correct = False
for i in range(len(instrs)):
  test_instrs = deepcopy(instrs)
  if instrs[i][0] == 'jmp':
    test_instrs[i][0] = 'nop'
  elif instrs[i][0] == 'nop':
    test_instrs[i][0] = 'jmp'
  else:
    next;
  accum, pos = run_program(test_instrs)
  if pos == len(test_instrs):
    terminate_correct = True
    break

print(terminate_correct)
print(accum, pos)
    
    

