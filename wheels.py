"""" The Wheels on the Bus Lyrics Generator
    Reference: https://bussongs.com/songs/wheels-on-the-bus-go-round-and-round
"""

CLOSING = "all through the town."


def verse(noun, verb, phrase):
    opening = f"The {noun} on the bus {verb} {phrase},"
    print(opening)
    print(phrase + ",")
    print(phrase + ".")
    print(opening)
    print(CLOSING)
    print()


def song():
    nouns = [
        'wheels', 'people', 'horn',
        'wipers', 'signals', 'motor',
        'babies', 'parents', 'mommy',
    ]

    verbs = ['go', 'go', 'goes']
    verbs += verbs
    verbs += ['go', 'go', 'says']

    def double(word):
        return f"{word} and {word}"

    def triple(word):
        return ', '.join(3 * (word,))

    phrases = [
        double('round'),
        'up and down',
        triple('beep'),
        triple('swish'),
        triple('blink'),
        triple('zoom'),
        triple('waa'),
        triple('shh'),
        'I love you',
    ]

    for n, v, p in zip(nouns, verbs, phrases):
        verse(n, v, p)


if __name__ == "__main__":
    song()
