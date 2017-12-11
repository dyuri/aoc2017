from functools import reduce
import re

GROUPS = []
with open('groups.txt') as f:
    GROUPS = f.readlines()


def split_group(grp):
    count = 0
    groups = []
    current = ''
    for i in grp:
        if i == '{':
            count += 1
            current += i
        elif i == '}':
            count -= 1
            current += i
        elif i == ',':
            if count == 0:
                groups.append(current)
                current = ''
            else:
                current += i
        else:
            current += i

    groups.append(current)

    return groups


def process_group(group, depth=0):
    current_depth = depth + 1

    inner = group[1:-1]

    # step 1 - apply !
    inner = re.sub(r'!.', '', inner)

    # step 2 - remove garbage
    inner = re.sub(r'<.*?>', '', inner)

    # inner groups # NEM JO "{{{{}}}},{}"
    if inner == "":
        return current_depth

    subgroups = split_group(inner)

    try:
        return current_depth + reduce(
            lambda p, c: p + process_group(c, current_depth),
            subgroups,
            0
        )
    except:
        print('error :: inner: {}'.format(inner))


if __name__ == "__main__":
    res = 0
    for g in GROUPS:
        res += process_group(g)

    print("total score: {}".format(res))
