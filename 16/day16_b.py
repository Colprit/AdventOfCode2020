with open('day16_input.txt') as f:
    rules_data, your_ticket, nearby_tickets = f.read().split('\n\n')

your_ticket = [int(f) for f in your_ticket.split('\n')[1].split(',')]
nearby_tickets = nearby_tickets.split('\n')[1:-1]

rules = {}
for rule in rules_data.split('\n'):
    rule_name, ranges = rule.split(': ')
    ranges = [[int(n) for n in r.split('-')] for r in ranges.split(' or ')]
    rules.update({ rule_name : ranges })

valid_ranges = [r for ranges in rules.values() for r in ranges]

nearby_tickets = [[int(field) for field in ticket.split(',')] for ticket in nearby_tickets]

valid_tickets = []

for ticket in nearby_tickets:
    valid_ticket = True
    for field in ticket:
        valid_field = False
        for r in valid_ranges:
            r1, r2 = r
            if r1 <= field <= r2:
                valid_field = True
                break
        if not valid_field:
            valid_ticket = False
            break
    if valid_ticket:
        valid_tickets.append(ticket)

field_possible = {}

remaining = set(range(len(rules)))

for rule_name, rule in rules.items():
    r1, r2 = rule
    possible = []
    for i in remaining:
        rule_broken = False
        for ticket in valid_tickets:
            if not r1[0] <= ticket[i] <= r1[1] and not r2[0] <= ticket[i] <= r2[1]:
                rule_broken = True
                break
        if not rule_broken:
            possible.append(i)
    field_possible.update({rule_name: set(possible)})

field_dict = {}

while len(field_dict) < 20:
    for field in field_possible:
        field_possible[field] = field_possible[field].intersection(remaining)
    
    for field, possible in field_possible.items():
        if len(possible) == 1:
            must_be = list(possible)[0]
            field_dict.update({ field : must_be })
            remaining.remove(must_be)

ans = 1
for field, pos in field_dict.items():
    if 'departure' in field:
        ans *= your_ticket[pos]

print(ans)