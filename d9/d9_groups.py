GROUPS = []
with open('groups.txt') as f:
    GROUPS = f.readlines()


def process_group(group):
    score = 0
    depth = 1
    garbage_count = 0
    is_garbage = False
    ignore_next = False
    for i in group:
        if ignore_next:
            ignore_next = False
        elif i == '!':
            ignore_next = True
        elif is_garbage and i != '>':
            garbage_count += 1
        elif i == '<':
            is_garbage = True
        elif i == '>':
            is_garbage = False
        elif i == '{':
            score += depth
            depth += 1
        elif i == '}':
            depth -= 1

    return score, garbage_count


if __name__ == "__main__":
    res = 0
    garbage = 0
    for g in GROUPS:
        (dres, dgarbage) = process_group(g)
        res += dres
        garbage += dgarbage

    print("total score: {}, garbage: {}".format(res, garbage))
