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

    go = ['go']
    gogo = go + go
    verbs = gogo
    verbs.append('goes')
    verbs += verbs
    verbs += gogo
    verbs += 'says'

    def pair(word1, word2=None):
        if not word2:
            word2 = word1
        return f"{word1} and {word2}"

    def triple(word):
        return ', '.join(3 * (word,))

    phrases = [
        pair('round'),
        pair('up', 'down'),
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
