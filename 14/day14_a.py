with open('day14_input.txt') as f:
    instrs = f.read().split('\n')[:-1]

def apply_mask(num, mask):
    num_bin = format(num, '036b')
    num_masked = ''.join(n if m == 'X' else m for m,n in zip(mask, num_bin))
    return int(num_masked, 2)

mask = 'X'*36
mem = {}
for instr in instrs:
    op, val = instr.split(' = ')
    if op == 'mask':
        mask = val
    else:
        addr = int(op[4:-1])
        mem.update({addr: apply_mask(int(val), mask)})

print(sum(mem.values()))
