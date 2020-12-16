with open('day16_input.txt') as f:
    rules_data, your_ticket, nearby_tickets = f.read().split('\n\n')

your_ticket = [int(f) for f in your_ticket.split('\n')[1].split(',')]
nearby_tickets = nearby_tickets.split('\n')[1:-1]

print(your_ticket)

rules = {}
for rule in rules_data.split('\n'):
    rule_name, ranges = rule.split(': ')
    ranges = [[int(n) for n in r.split('-')] for r in ranges.split(' or ')]
    rules.update({ rule_name : ranges })

valid_ranges = []
for range_pair in rules.values():
    for r in range_pair:
        valid_ranges.append(r)

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

field_dict = {}

remaining = set(range(len(rules)))

for rule_name, rule in rules.items():
    r1, r2 = rule
    for i in remaining:
        rule_broken = False
        for ticket in valid_tickets:
            if not r1[0] <= ticket[i] <= r1[1] and not r2[0] <= ticket[i] <= r2[1]:
                rule_broken = True
                break
        if not rule_broken:
            break
    field_dict.update({ rule_name : i })
    remaining.remove(i)

print(field_dict)

ans = 1
for field, pos in field_dict.items():
    if 'departure' in field:
        ans *= your_ticket[pos]
        print(your_ticket[pos])

print(ans)