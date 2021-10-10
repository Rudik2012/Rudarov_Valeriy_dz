words = {
    "one":"один",
    "two":"два",
    "three":"три",
    "four":"четыре",
    "five":"пять",
    "six":"шесть",
    "seven":"семь",
    "eight":"восемь",
    "nine":"девять",
    "ten":"десять"
}


def num_translate_adv(key):
    if key.istitle():
        print(f'"{str(words.get(key.lower())).title()}"')
    else:
        print(f'"{words.get(key)}"')

num_translate_adv("To")











