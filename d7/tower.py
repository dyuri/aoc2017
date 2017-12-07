import re

PROGS = []

with open('tower.txt') as f:
    PROGS = [j.strip() for j in f.readlines()]


class Prog():

    PROGS = {}

    @staticmethod
    def from_line(line):
        line_data = re.sub(r'[^\w]+', ' ', line).split()
        return Prog(line_data[0], int(line_data[1]), line_data[2:])

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children_names = children
        self.children = []
        self.parent = None

        self.PROGS[name] = self

    def __str__(self):
        return "{self.name} ({self.weight}) -> {children}".format(
            self=self,
            children=', '.join([p.name for p in self.children])
        )

    def __repr__(self):
        return str(self)

    def sum_weight(self):
        return self.weight + sum([ch.sum_weight() for ch in self.children])

    def resolve_children(self):
        for chn in self.children_names:
            self.children.append(self.PROGS[chn])
            self.PROGS[chn].parent = self


def inspect(node, ref=None):
    # print("node: {}, node sum weight: {}".format(node, node.sum_weight()))
    chweights = {}
    for ch in node.children:
        sw = ch.sum_weight()
        chweights[sw] = chweights.get(sw, []) + [ch]

    print("children: {}".format(chweights))
    if len(chweights) == 1:
        print("children are OK, node name: {}, ref: {}, new weight: {}".format(
            node.name,
            ref,
            node.weight - (node.sum_weight() - ref)
        ))
    else:
        # 2 different weights
        wrong = None
        refw = None
        chws = list(chweights.keys())
        if len(chweights[chws[0]]) == 1:
            wrong = chweights[chws[0]][0]
            refw = chws[1]
        else:
            wrong = chweights[chws[1]][0]
            refw = chws[0]

        print("wrong node: {}, siblings weight: {}".format(wrong, refw))
        inspect(wrong, refw)


PROGS = list([Prog.from_line(l) for l in PROGS])

for p in PROGS:
    p.resolve_children()

ROOT = None

for p in PROGS:
    if not p.parent:
        ROOT = p
        print("root: %s" % p)

inspect(ROOT)
