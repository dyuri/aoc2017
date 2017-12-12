from functools import reduce

ITEMS = list(range(0, 256))

INPUTTXT = "192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"
EXTRA = [17, 31, 73, 47, 23]

INPUT = [ord(ch) for ch in INPUTTXT] + EXTRA

current = 0
skip = 0


def get_sublist(items, current, input):
    to = current + input

    if to <= len(items):
        return items[current:to]
    else:
        to = to % len(items)
        return items[current:] + items[:to]


def replace_items(items, replacement, current):
    for i in replacement:
        items[current] = i
        current = (current + 1) % len(items)


def knot(items, current, skip, input):
    sublist = reversed(get_sublist(items, current, input))

    replace_items(items, sublist, current)

    current = (skip + current + input) % len(items)
    skip += 1

    return current, skip


# 64 rounds of knot
for x in range(0, 64):
    for i in INPUT:
        (current, skip) = knot(ITEMS, current, skip, i)

# convert to hash
HASH = []
for i in range(0, 256, 16):
    HASH.append(reduce(lambda x, y: x ^ y, ITEMS[i:i+16], 0))

HEXDIGEST = "".join("{:02x}".format(h) for h in HASH)

print(HEXDIGEST)
