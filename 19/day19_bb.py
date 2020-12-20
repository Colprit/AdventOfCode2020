with open('day19_input_b.txt') as f:
    rules_raw, msgs = f.read().split('\n\n')

rules = {int(rule.split(': ')[0]) : rule.split(': ')[1] for rule in rules_raw.split('\n')}
msgs = msgs.split('\n')

MAX = max([len(msg) for msg in msgs])

for name in rules.keys():
    rule = rules[name]
    if '"' in rule:
        _rule = rule[1:-1]
    else:
        _rule = [[int(r) for r in part.split(' ')] for part in rule.split(' | ')]
    rules.update({name : _rule})

# evaluated = {name:isinstance(rule, str) for name, rule in rules.items()}
evaluated = [name for name, rule in rules.items() if isinstance(rule, str)]

for eval_name in evaluated:
    eval_rule = rules[eval_name]
    for name, rule in rules.items():
        for part in rule:
            
            


total = 0
for msg in msgs:
    if msg in rules[0]:
        total += 1

print(total)