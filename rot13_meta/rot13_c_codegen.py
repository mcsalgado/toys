print('''#include <stdio.h>

char *stream;

void rot13()
{
    switch (*stream) {''')

for i in range(ord('A'), ord('Z')+1):
    j = ((i - ord('A') + 13) % (ord('Z') - ord('A') + 1)) + ord('A')
    print(f"    case '{chr(i)}':")
    print(f"        *stream++ = '{chr(j)}';")
    print(f"        return;")

for i in range(ord('a'), ord('z')+1):
    j = ((i - ord('a') + 13) % (ord('z') - ord('a') + 1)) + ord('a')
    print(f"    case '{chr(i)}':")
    print(f"        *stream++ = '{chr(j)}';")
    print(f"        return;")

print('''    default:
        *stream++;
        return;
    }
}

int main(int argc, char **argv)
{
    char source[1024];
    scanf("%s", source);

    stream = source;
    while (*stream) {
        rot13();
    }

    printf(source);

    return 0;
}''')
