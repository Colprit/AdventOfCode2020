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

evaluated = []

def eval_rule(name):
    global rules
    rule = rules[name]
    if all([isinstance(r, str) for r in rule]):
        return
    else:
        all_opts = []
        for part in rule:
            opts = ['']
            for r in part:
                eval_rule(r)
                opts = [opt+x for opt in opts for x in rules[r]]
                opts = [opt for opt in opts if len(opt) <= MAX]
            all_opts += opts
        rules[name] = all_opts

eval_rule(0)
print('len', len(rule[0]))
print('rule', rule[0])

total = 0
for msg in msgs:
    if msg in rules[0]:
        total += 1

print(total)