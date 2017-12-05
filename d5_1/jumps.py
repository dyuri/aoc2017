JUMPS = []

with open('stack.txt') as f:
    JUMPS = [int(j.strip()) for j in f.readlines()]

pos = 0
steps = 0

try:
    while True:
        next = JUMPS[pos]
        JUMPS[pos] += 1
        pos = next + pos
        steps += 1
except IndexError:
    print('steps required: %s' % steps)
