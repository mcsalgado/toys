print('''#!/usr/bin/env python3


def rot13(c):''')

for i in range(ord('A'), ord('Z')+1):
    j = ((i - ord('A') + 13) % (ord('Z') - ord('A') + 1)) + ord('A')
    print(f"    if c == '{chr(i)}':")
    print(f"        return '{chr(j)}'")

for i in range(ord('a'), ord('z')+1):
    j = ((i - ord('a') + 13) % (ord('z') - ord('a') + 1)) + ord('a')
    print(f"    if c == '{chr(i)}':")
    print(f"        return '{chr(j)}'")

print('''

if __name__ == '__main__':
    print(''.join(map(rot13, input())))''')
