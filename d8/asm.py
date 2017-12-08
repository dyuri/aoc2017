INSTRUCTIONS = []
HIGHEST_EVER = 0


class Instruction():

    def __init__(self, line):
        l = line.split()

        self.reg = l[0]
        self.op = l[1]
        self.op_p = int(l[2])
        self.cond_reg = l[4]
        self.cond = l[5]
        self.cond_p = int(l[6])

    def run(self):
        reg = REGS.get(self.reg, 0)
        cond_reg = REGS.get(self.cond_reg, 0)
        op = OPS[self.op]
        cond = OPS[self.cond]

        if cond(cond_reg, self.cond_p):
            val = op(reg, self.op_p)
            REGS[self.reg] = val
            return val

        return reg


with open('instructions.txt') as f:
    INSTRUCTIONS = [Instruction(l) for l in f.readlines()]

REGS = {}

OPS = {
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y,
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y
}


for inst in INSTRUCTIONS:
    HIGHEST_EVER = max(inst.run(), HIGHEST_EVER)

print('registers: {}'.format(REGS))
print('max value: {}'.format(max(REGS.values())))
print('highest ever: {}'.format(HIGHEST_EVER))
