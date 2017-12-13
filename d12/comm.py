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

node0 = comms[0]
processed0 = node0["processed"]
remaining0 = node0["remaining"]

while len(remaining0):
    next = remaining0.pop()
    processed0.add(next)
    nextcomms = comms[next]
    nextproc = nextcomms["processed"]
    nextrem = nextcomms["remaining"]
    newcomms = nextrem.difference(processed0)
    remaining0.update(newcomms)

print(len(processed0))
