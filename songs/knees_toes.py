""" Knees and Toes Lyrics Generator
    Reference: https://en.wikipedia.org/wiki/Head,_Shoulders,_Knees_and_Toes
"""


def write_line(parts, char):
    line = ', '.join(parts[:-1])
    line += ' and '
    line += parts[-1]
    print(line + char)


def do_ands(parts):
    for p in parts:
        print('and ' + p + ' ', end="")
    print()


def song():
    parts1 = ['Head', 'shoulders', 'knees', 'toes']
    parts2 = ['eyes', 'ears', 'mouth', 'nose']

    def chorus():
        write_line(parts1, ',')
        write_line(parts1[-2:], '!')

    for _ in range(2):
        chorus()
    do_ands(parts2)
    chorus()


if __name__ == "__main__":
    song()
