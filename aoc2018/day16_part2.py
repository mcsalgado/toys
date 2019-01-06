import fileinput
from inspect import isfunction

import day16_instructions

# NOTE(mcsalgado): hardcoded opcodes obtained from running the generated prolog
SOLUTION = (12, 14, 7, 3, 10, 15, 5, 6, 0, 9, 13, 2, 8, 4, 11, 1)

instructions = {k: v
                for k, v in day16_instructions.__dict__.items()
                if isfunction(v)}

to_instruction_fn = dict(zip(SOLUTION, instructions.values()))

lines = iter(line.strip() for line in fileinput.input())

# NOTE(mcsalgado): hacky way to skip to the second section of the input
while True:
    l0, l1 = next(lines), next(lines)
    if l0 == l1 == '':
        break

registers = (0, 0, 0, 0)
for line in lines:
    opcode, a, b, c = tuple(map(int, line.strip().split()))
    registers = to_instruction_fn[opcode](registers, a, b, c)

print(registers[0])
