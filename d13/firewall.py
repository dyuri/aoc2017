FW = """0: 3
1: 2
4: 4
6: 4"""

FW = open("firewall.txt", "r").read().strip()

fw = [tuple(l.split(": ")) for l in FW.split("\n")]

severity = 0

for rule in fw:
    layer = int(rule[0])
    range = int(rule[1])
    if layer % (2 * range - 2) == 0:
        severity += layer * range

print(severity)

wait = 0

while True:
    wait += 1
    ok = True

    for rule in fw:
        layer = int(rule[0])
        range = int(rule[1])
        if (layer + wait) % (2 * range - 2) == 0:
            ok = False
            break

    if ok:
        break

print("wait: {}".format(wait))
