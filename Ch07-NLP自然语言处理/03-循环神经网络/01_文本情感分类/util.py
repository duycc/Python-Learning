import re


def tokenlize(sentence: str):
    fileters = [
        '!',
        '"',
        '#',
        '$',
        '%',
        '&',
        '\(',
        '\)',
        '\*',
        '\+',
        ',',
        '-',
        '\.',
        '/',
        ':',
        ';',
        '<',
        '=',
        '>',
        '\?',
        '@',
        '\[',
        '\\',
        '\]',
        '^',
        '_',
        '`',
        '\{',
        '\|',
        '\}',
        '~',
        '\t',
        '\n',
        '\x97',
        '\x96',
        '”',
        '“',
    ]
    sentence = sentence.lower()
    sentence = re.sub("<br />", " ", sentence)
    sentence = re.sub("|".join(fileters), " ", sentence)
    tokens = [word for word in sentence.split(" ") if len(word) > 0]
    return tokens
