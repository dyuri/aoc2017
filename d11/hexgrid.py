from collections import Counter

steps = open('hexgrid.txt', 'r').read().strip().split(',')

x, y, z = 0, 0, 0


def hex_dist(x, y, z):
    return (abs(x) + abs(y) + abs(z)) / 2


distances = []

for step in steps:
    if step == "n":
        y += 1
        z -= 1
    elif step == "s":
        y -= 1
        z += 1
    elif step == "ne":
        x += 1
        z -= 1
    elif step == "sw":
        x -= 1
        z += 1
    elif step == "nw":
        x -= 1
        y += 1
    elif step == "se":
        x += 1
        y -= 1

    distances.append(hex_dist(x, y, z))

dist = hex_dist(x, y, z)
print("distance: {}, max: {}".format(dist, max(distances)))
