COMMS = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

COMMS = open("comm.txt", "r").read().strip()


def parse_comm(line):
    node, friendlist = tuple(line.split(" <-> "))

    return int(node), {int(f) for f in friendlist.split(", ")}


comms = {}
for l in COMMS.split("\n"):
    node, friends = parse_comm(l)
    comms[node] = {
                "processed": {node},
                "remaining": friends
            }

groups = []
while len(comms):
    key0, node0 = comms.popitem()
    processed0 = node0["processed"]
    remaining0 = node0["remaining"]

    while len(remaining0):
        next = remaining0.pop()
        processed0.add(next)
        if next in comms:
            nextcomms = comms[next]
            nextproc = nextcomms["processed"]
            nextrem = nextcomms["remaining"]
            newcomms = nextrem.difference(processed0)
            remaining0.update(newcomms)
            del comms[next]

    groups.append(node0)
    if key0 in comms:
        del comms[key0]

print("size of group 0: {}".format([
    len(g["processed"]) for g in groups if 0 in g["processed"]
]))
print("groups: {}".format(len(groups)))
