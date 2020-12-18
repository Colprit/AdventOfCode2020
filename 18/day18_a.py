with open('day18_input.txt') as f:
    eqns = f.read().replace(' ','').split('\n')


def find_closing_bracket(eqn):
    level = -1
    for i in range(len(eqn)):
        if eqn[i] == '(':
            level += 1
        elif eqn[i] == ')':
            if level == 0:
                return i
            else:
                level -= 1
    return 'error'


def calc(total, eqn):
    if len(eqn) == 0:
        return total

    op = eqn[0]

    if eqn[1] == '(':
        bracket_close = find_closing_bracket(eqn)
        x = start_calc(eqn[2:bracket_close])
        eqn_remain = eqn[bracket_close+1:]
    else:
        x = int(eqn[1])
        eqn_remain = eqn[2:]

    if op == '+':
        return calc(total+x, eqn_remain)
    elif op == '*':
        return calc(total*x, eqn_remain)
    else:
        print('ERROR')
        return 0

def start_calc(eqn):
    return calc(1, '*'+eqn)

total = sum([start_calc(eqn) for eqn in eqns])

print(total)
