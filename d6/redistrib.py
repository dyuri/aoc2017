from math import ceil

BANKS = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

HISTORY = []


def banks_to_str(banks):
    return '|'.join(map(str, banks))


def store(banks):
    HISTORY.append(banks_to_str(banks))


def seen(banks):
    return banks_to_str(banks) in HISTORY


def redistrib(banks):
    m = max(banks)
    i = banks.index(m)

    banks[i] = 0

    for j in range(i-len(banks)+1, i+1):
        diff = ceil(m / (i-j+1))
        banks[j] += diff
        m -= diff


if __name__ == '__main__':
    step = 0
    while not seen(BANKS):
        store(BANKS)
        step += 1
        redistrib(BANKS)

    print('steps required: %s' % step)
    print('cycle size: %s' % (step - HISTORY.index(banks_to_str(BANKS))))
