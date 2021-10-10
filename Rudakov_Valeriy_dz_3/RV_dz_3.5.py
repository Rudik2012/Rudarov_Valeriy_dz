from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    """
    :param n: количество шуток
    :return: список случайных шуток
    """

    jokes = []
    len_jokes = min(len(nouns), len(adverbs), len(adjectives))
    while n != 0 and len_jokes != 0:
        a = randrange(len_jokes)
        jokes.append(f"{nouns.pop(a)} {adverbs.pop(a)} {adjectives.pop(a)}")
        n -= 1
        len_jokes -= 1
    return jokes

print(get_jokes(7))