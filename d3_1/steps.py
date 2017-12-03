from math import ceil, sqrt

num = 277678


def reqsteps(num):
    if num == 1:
        return 0

    box = (ceil(sqrt(num)) // 2) * 2 + 1
    boxsteps = (box - 1) // 2
    biggest = box**2
    diff = (biggest - num) % (box-1)
    edgesteps = abs(diff - boxsteps)
    steps = boxsteps + edgesteps

    print('num: %s' % num)
    print('%sth box, steps required: %s' % (box, boxsteps))
    print('biggest member of box is: %s' % biggest)
    print('biggest - num mod boxsize: %s' % diff)
    print('steps on the edge: %s' % edgesteps)
    print('steps together: %s' % steps)


reqsteps(num)
