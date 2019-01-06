import fileinput
from inspect import isfunction

import day16_instructions

instructions = {k: v
                for k, v in day16_instructions.__dict__.items()
                if isfunction(v)}

lines = iter(line.strip() for line in fileinput.input())

samples = []
while True:
    next_lines = next(lines)
    if next_lines == '':
        break

    _, before = next_lines.split(': ')
    before = tuple(map(int, before[1:-1].split(', ')))

    instruction_statement = tuple(map(int, next(lines).split()))

    _, after = next(lines).split(': ')
    after = after.strip()
    after = tuple(map(int, after[1:-1].split(', ')))

    samples.append((instruction_statement, before, after))

    assert next(lines) == ''

answer = 0
for (opcode, input_a, input_b, output), before, after in samples:
    t = 0
    for instruction_fn in instructions.values():
        if instruction_fn(before, input_a, input_b, output) == after:
            t += 1
    if t >= 3:
        answer += 1

print(answer)
