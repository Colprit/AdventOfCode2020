with open('day14_input.txt') as f:
    instrs = f.read().split('\n')[:-1]

def apply_mask(num, mask):
    num_bin = format(num, '036b')
    masked = ''.join(n if m == '0' else m for m,n in zip(mask, num_bin))
    k = masked.count('X')
    masked = masked.replace('X', '{}')
    masked_opts = []
    for i in range(2**(k)):
        vals = list(format(i, f'0{str(k)}b'))
        masked_opts.append(masked.format(*vals))
    return [int(opt,2) for opt in masked_opts]

mask = 'X'*36
mem = {}
for instr in instrs:
    op, val = instr.split(' = ')
    if op == 'mask':
        mask = val
    else:
        addrs = apply_mask(int(op[4:-1]), mask)
        mem.update({addr: int(val) for addr in addrs})

print(sum(mem.values()))
