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

evaluated = {name:isinstance(rule, str) for name, rule in rules.items()}

def eval_rule(name, K):
    global rules
    print(K)
    if K == 0:
        return ['']
    if not evaluated[name]:
        rule = rules[name]
        all_opts = []
        for part in rule:
            opts = ['']
            for r in part:
                if evaluated[r]:
                    X = rules[r]
                else:
                    X = eval_rule(r, K-1)
                    evaluated[r] = True
                opts = [opt+x for opt in opts for x in X if len(opt+x) <= MAX]
            all_opts += opts
        rules[name] = all_opts
        # print(name, ':', all_opts)
        return all_opts

eval_rule(0,MAX)
print('len', len(rule[0]))
print('rule', rule[0])

total = 0
for msg in msgs:
    if msg in rules[0]:
        total += 1

print(total)