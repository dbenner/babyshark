""" Baby Shark Lyrics Generator """

doodoo = ' '.join(6 * ('doo',))


def verse(phrase):
    for _ in range(3):
        print(f"{phrase}, {doodoo}.")
    print(f"{phrase}!")
    print()


def song():
    for member in ['Baby', 'Mommy', 'Daddy', 'Grandma', 'Grandpa']:
        verse(f"{member} Shark")
    for phrase in ["Let's go hunt", "Run away", "Safe at last", "It's the end"]:
        verse(phrase)


if __name__ == "__main__":
    song()
