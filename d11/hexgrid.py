STEPS = 'ne,ne,s,s'.replace(',', '')

DIRECTIONS = {}

for s in STEPS:
    DIRECTIONS[s] = DIRECTIONS.get(s, 0) + 1

s = DIRECTIONS.get('s', 0)
n = DIRECTIONS.get('n', 0)
e = DIRECTIONS.get('e', 0)
w = DIRECTIONS.get('w', 0)
dsn = abs(s - n)
dew = abs(e - w)
steps = max(dsn-min(e, w), dew)

print("steps: {}".format(steps))
