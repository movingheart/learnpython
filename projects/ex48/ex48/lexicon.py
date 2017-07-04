# -*- coding:utf-8 -*-


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(stuff):
    directions = ("north", "south", "east", "west", "down", "up", "left", "right", "back")
    verbs = ("go", "stop", "kill", "eat")
    preps = ("the", "in", "of", "from", "at", "it")
    nouns = ("door", "bear", "princess", "cabinet")
    numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    words = stuff.split()
    results = []
    for word in words:
        temp_tup = ()
        if word in directions:
            temp_tup = ('direction', word)
        elif word in verbs:
            temp_tup = ('verb', word)
        elif word in nouns:
            temp_tup = ('noun', word)
        elif word in preps:
            temp_tup = ('stop', word)
        elif convert_number(word):
            temp_tup = ('number', int(word))
        else:
            temp_tup = ('error', word)
        results.append(temp_tup)
    return results
