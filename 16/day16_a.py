with open('day16_input.txt') as f:
    rules_data, your_ticket, nearby_tickets = f.read().split('\n\n')

your_ticket = your_ticket.split('\n')[1:]
nearby_tickets = nearby_tickets.split('\n')[1:-1]

rules = {}
for rule in rules_data.split('\n'):
    rule_name, ranges = rule.split(': ')
    ranges = [[int(n) for n in r.split('-')] for r in ranges.split(' or ')]
    rules.update({ rule_name : ranges })

valid_ranges = [r for ranges in rules.values() for r in ranges]

all_nearby_fields = [int(field) for ticket in nearby_tickets for field in ticket.split(',')]

total = 0

for f in all_nearby_fields:
    valid = False
    for r in valid_ranges:
        r1, r2 = r
        if r1 <= f <= r2:
            valid = True
            break
    if not valid:
        total += f

print(total)
