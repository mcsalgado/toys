import fileinput

import jinja2

cat = ''.join

rot13_table = {}
for i in range(ord('A'), ord('Z')+1):
    j = ((i - ord('A') + 13) % (ord('Z') - ord('A') + 1)) + ord('A')
    rot13_table[chr(i)] = chr(j)

for i in range(ord('a'), ord('z')+1):
    j = ((i - ord('a') + 13) % (ord('z') - ord('a') + 1)) + ord('a')
    rot13_table[chr(i)] = chr(j)

template = cat(fileinput.input())
env = jinja2.Environment(trim_blocks=True,
                         autoescape=False)

print(cat(env.from_string(template).stream(**locals())))
