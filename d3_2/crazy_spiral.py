from math import ceil, sqrt
from functools import reduce


def spiral_at_pos(pos):

    if pos == 1:
        return 1

    coord = pos_to_coord(pos)
    neighbours = sorted(filter(lambda x: x < pos,
                        map(coord_to_pos, [
                            (coord[0]+1, coord[1]+1),
                            (coord[0]+1, coord[1]),
                            (coord[0]+1, coord[1]-1),
                            (coord[0], coord[1]+1),
                            (coord[0], coord[1]-1),
                            (coord[0]-1, coord[1]+1),
                            (coord[0]-1, coord[1]),
                            (coord[0]-1, coord[1]-1),
                        ])))

    print('meg nem jo, 10-nel elcsuszik')

    value = reduce(lambda p, c: p + spiral_at_pos(c), neighbours)

    return value


def coord_to_pos(coord):
    x = coord[0]
    y = coord[1]
    pos = 1

    if x == 0 and y == 0:
        return pos

    box = abs(x) if abs(x) > abs(y) else abs(y)

    inner = (2 * box - 1)**2

    side = 2 * box

    if abs(x) == box and x < 0 and x != y:
        # bottom
        pos = inner + 3 * side + side//2 + y
    elif abs(y) == box and y < 0 and y != -x:
        # left
        pos = inner + 2 * side + side//2 - x
    elif abs(x) == box and x > 0 and x != y:
        # top
        pos = inner + side + side//2 - y
    else:  # abs(y) == box and y > 0:
        # right
        pos = inner + side//2 + x

    return pos


def pos_to_coord(pos):
    x = 0
    y = 0

    if pos == 1:
        return (x, y)

    box = (ceil(sqrt(pos)) // 2) * 2 + 1
    biggest = box**2
    diff = biggest - pos
    sidenum = diff // (box-1)

    if sidenum == 3:
        # right
        y = (box-1) // 2
        x = (box-1)//2 - diff % (box-1)
    elif sidenum == 2:
        # top
        x = (box-1) // 2
        y = - ((box-1)//2 - diff % (box-1))
    elif sidenum == 1:
        # left
        y = - (box-1) // 2
        x = - ((box-1)//2 - diff % (box-1))
    else:  # sidenum == 0
        # bottom
        x = - (box-1) // 2
        y = (box-1)//2 - diff % (box-1)

    return (x, y)
