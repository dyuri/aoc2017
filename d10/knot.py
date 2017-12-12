ITEMS = list(range(0, 256))

INPUT = [
    192,
    69,
    168,
    160,
    78,
    1,
    166,
    28,
    0,
    83,
    198,
    2,
    254,
    255,
    41,
    12
]

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


for i in INPUT:
    (current, skip) = knot(ITEMS, current, skip, i)


print('first two: {} * {} = {}'.format(
    ITEMS[0],
    ITEMS[1],
    ITEMS[0] * ITEMS[1]
))
